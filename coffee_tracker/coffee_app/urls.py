# coffee_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('receive/<int:person_id>/', views.receive_coffee, name='receive-coffee'),
    path('purchase/<int:person_id>/', views.purchase_coffee, name='purchase-coffee'),
    path('createperson/', views.create_person, name='create-person'),
    path('deleteperson/<int:person_id>/', views.delete_person, name='delete-person')
] 