from django.forms import ModelForm
from .models import Business
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Business_Form(ModelForm):
    class Meta:
      model = Business 
      labels = {'name': "Business Name"}
      fields = ['name','address_1', 'address_2', 'city','state', 'zipcode', 'phone_number',
      'description', 'email', 'website']

class Review_Form(ModelForm): 
    class Meta: 
      model = Review
      fields = ['title' ,'review' ]

# class Signup_Form(UserCreationForm):
#     email = forms.EmailField(label='Email')
#     first_name = forms.CharField(label='First Name')
#     last_name = forms.CharField(label= 'Last Name')
#     class Meta:
#       model = User
#       fields = ['email', 'first_name', 'last_name']

class Signup_Form(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

        



       









