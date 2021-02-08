from django.shortcuts import render
from django.http import HttpResponse
from .models import Business

# Create your views here.


#===============home page =================
def home(request):
    return render(request, 'home.html')

#============= ==============






