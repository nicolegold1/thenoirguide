from django.forms import ModelForm
from .models import Business
from .models import Review


class Business_Form(ModelForm):
    class Meta:
      model = Business 
      labels = {'name': "Business Name"}
      fields = ['name','address_1', 'address_2', 'city','state', 'zipcode', 'phone_number',
      'description', 'email', 'website']

class Review_Form(ModelForm): 
    class Meta: 
      model = Review
      fields = ['business', 'review', 'user']


       









