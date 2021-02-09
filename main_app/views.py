from django.shortcuts import render
from django.http import HttpResponse
from .models import Business

# Create your views here.


#===============Home page ===============

def home(request):
    return render(request, 'home.html')







#=============Business page ==============

def review_index(request):
    if request.method == 'POST':
        review_form = Review_Form(request.POST)
        if review_form.is_valid():
            # Add the user from the request object before saving
            new_review = business_form.save(commit=False)
            new_review.user = request.user
            new_review.save()
            return redirect('review_index')
    reviews = Review.objects.all()
    review_form = Review_Form()
    context = {'reviews': reviews, 'review_form': review_form}
    return render(request, 'reviews/index.html', context)



#============Review page =================







