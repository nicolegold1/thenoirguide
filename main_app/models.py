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
    phone_number = models.CharField(max_length=22, blank=True )
    description = models.TextField(max_length=700)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length= 100, blank=True)
    category = models.CharField(max_length=15, default=[0][0])


    def __str__(self):
       return self.name


CATEGORY_LIST = [
        ('REST', 'Restarant'),
        ('HAIR', 'Hair Salon'),
        ('BARB', 'Barber Shop'),
        ('ESTH', 'Esthetician'),
        ('NAIL'   'Nail Salon'),
        ('DERM', 'Dermatologist'),
        ('APPL', 'Appliance Repair'),
        ('LAWY', 'Lawyer'),
        ('EVEN', 'Event Planner'),
        ('REAL', 'REALTOR'),
        ('SKIN',  'Skincare')
 ]

category_type = models.CharField(
        max_length=4,
        choices=CATEGORY_LIST,
        default=CATEGORY_LIST[0][0]
    )


    



   



    
  
    





