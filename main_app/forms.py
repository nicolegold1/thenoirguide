from django.forms import ModelForm
from .models import Business, business_types

class Business_Form(ModelForm):
    class Meta:
      model = Business 
      labels = {'name': "Business Name"}
      fields = ['name','breed','description', 'age']

class Business_type_Form(ModelForm): 
    class Meta: 
      model = Feeding 
      fields = ['date', 'meal']