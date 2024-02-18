from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  Reservation(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=20)  # Changed to CharField
    date= models.DateField() 
    time = models.TimeField()  # Combined date and time into a single field
    no_of_people = models.IntegerField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class  Contact(models.Model):
    contact_name=models.CharField(max_length=200)
    contact_email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=200)
    contact_message=models.CharField(max_length=1000)

    def __str__(self):
        return self.contact_name