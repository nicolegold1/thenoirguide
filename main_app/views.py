from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


#===============Home page ===============


def home(request):
    return HttpResponse('<h1> About the Noir Guide</h1>')

def about(request):
    return render(request, 'about.html')

def reviews_index(request):
    reviews = Reviews.object.all()
    context = { 'reviews': reviews}
    return render(request, 'reviews/index.html', context)

def reviews_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    context = {'review': review}




#=============Review page ==============


 



#============Review page =================







