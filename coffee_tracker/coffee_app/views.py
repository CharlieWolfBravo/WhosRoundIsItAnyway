from django.shortcuts import render, redirect, get_object_or_404
from .models import Person

# Create your views here.
def home(request):
    people = sorted(Person.objects.all(), key= lambda p: p.get_owed(), reverse=True)
    top_debtor = people[0] if len(people) > 0 else None
    context = {'people': people,
               'top_debtor': top_debtor}
    return render(request, 'home.html', context)

def receive_coffee(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    # should be in a controller
    person.set_received(person.get_received() + 1)
    person.save()
    return redirect('home')

def purchase_coffee(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    # should be in a controller
    person.set_purchased(person.get_purchased() + 1)
    person.save()
    return redirect('home')

def create_person(request):
    # should be in a controller
    p = Person(name=request.POST.get('name'))
    p.save()
    return redirect('home')

def delete_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect('home')