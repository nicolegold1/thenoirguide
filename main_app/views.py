from django.shortcuts import render
from django.http import HttpResponse


from .models import Business
from .forms import Business_Form

# Create your views here.


#===============Home page ===============


def home(request):
    return HttpResponse('<h1> The Noir Guide</h1>')

def about(request):
    return render(request, 'about.html')

def business_index(request):
    if request.method == 'POST':
        business_form = Business_Form(request.POST)
        if business_form.is_valid():
            new_business = business_form.save()
            return redirect('business_index')
    business = Business.objects.all()
    context = {'business': business}
    return render(request, 'business/index.html', context)


def business_detail(request, business_id):
    business = Business.objects.filter(id=business_id)
    context = {'business': business}
    return render(request, 'business/detail.html', context)





#=============Review page ==============


 



#============Review page =================







