from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


#===============Home page ===============


def home(request):
    return HttpResponse('<h1> The Noir Guide</h1>')

def about(request):
    return render(request, 'about.html')






#=============Review page ==============


 



#============Review page =================







