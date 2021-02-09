from django.shortcuts import render
from django.http import HttpResponse


from .models import Business

# Create your views here.


#===============Home page ===============


def home(request):
    return HttpResponse('<h1> The Noir Guide</h1>')

def about(request):
    return render(request, 'about.html')

def business_index(request):
    business = Business.objects.all()
    context = {'business': business}
    return render(request, 'business/index.html', context)

    # def cats_index(request):
    #   return render(request, 'cats/index.html', { 'cats': cats })
    

    #   return render(request, 'reviews/index.html', { 'reviews': reviews })

# def reviews_detail(request, review_id):
#     review = Review.objects.get(id=review_id)
#     context = {'review': review}





#=============Review page ==============


 



#============Review page =================







