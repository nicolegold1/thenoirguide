from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone_number = models.IntegerField(blank=True )
    description = models.TextField(max_length=1000)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length= 100, blank=True)

   
   

    
  
    





