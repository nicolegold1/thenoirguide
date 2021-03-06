from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .models import Business
from .forms import Business_Form
from .models import Review
from .forms import Review_Form
from .forms import Signup_Form

# Create your views here.


#===============Home page ===============


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')


#=============Business Routes ==============

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
    reviews = Review.objects.filter(business_id=business_id)
    context = {'business': business,'reviews': reviews}
    return render(request, 'business/detail.html', context)


#=============Review Routes==============
@login_required
def review_index(request):
    if request.method == 'POST':
        review_form = Review_Form(request.POST)
        if review_form.is_valid():
                
                new_review = review_form.save(commit=False)
                new_review.user = request.user
                new_review.save()
                return redirect('review_index')
    review = Review.objects.filter(user=request.user)
    review_form = Review_Form()
    context = {'review': review, 'review_form': review_form}
    return render(request, 'review/index.html', context)

@login_required
def review_edit(request, review_id ):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        review_form = Review_Form(request.POST, instance=review)
        if review_form.is_valid(): 
            review_form.save()
            return redirect('business_index')

    review_form = Review_Form(instance=review)
    context = {'review_form': review_form, 'review': review}
    return render(request,'reviews/edit.html', context)

@login_required
def review_delete(request, review_id):
    Review.objects.get(id=review_id).delete()
    return redirect('business_index')

@login_required
def review_create(request, business_id):
    if request.method == 'POST':
        review_form = Review_Form(request.POST)
        if review_form.is_valid():
            business = Business.objects.get(id=business_id)
            author = request.user 
            review = Review 
            review = review_form.save(commit=False)
            review.user = author 
            review.business=business
            review.save()
            return redirect('business_index')
        else:
            current_user = request.user
            context = {'review_form': review_form ,'current_user': current_user}
            return render(request, 'reviews/create.html', context)
    else:
        review_form = Review_Form()
        current_user = request.user
        context = {'review_form': review_form ,'current_user': current_user, 'business_id': business_id}
        return render(request, 'reviews/create.html', context)

#=============Signup Route ==============


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form =UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('business_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

    









 










