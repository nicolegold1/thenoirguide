from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


#===============home page =================
def home(request):
    return render(request, 'home.html')

#============= ==============




