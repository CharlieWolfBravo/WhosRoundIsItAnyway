from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)  # Name of person
    coffees_purchased = models.IntegerField(default=0)  # Number of coffees this person has purchased.
    coffees_received = models.IntegerField(default=0)  # Number of coffees received.

    def __str__(self):
        return self.name
    
    def get_owed(self):
        return self.get_received() - self.get_purchased()
    
    def get_purchased(self):
        return self.coffees_purchased
    
    def get_received(self):
        return self.coffees_received
    
    def set_purchased(self, value):
        self.coffees_purchased = value
        return
    
    def set_received(self, value):
        self.coffees_received = value
        return
