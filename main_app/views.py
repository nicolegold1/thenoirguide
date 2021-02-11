from django.shortcuts import render
from django.http import HttpResponse


from .models import Business
from .forms import Business_Form
from .models import Review
from .forms import Review_Form

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
    reviews = Review.objects.filter(business_id=business_id)
    context = {'business': business,'reviews': reviews}
    return render(request, 'business/detail.html', context)

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


def review_edit(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        review_form = Review_Form(request.POST, instance=review)
        if review_form.is_valid(): 
            review_form.save()
            return redirect('business_detail', review_id=review.id)

    review_form = Review_Form(instance=review)
    context = {'review_form': review_form, 'review': review}
    return render(request,'reviews/edit.html', context)

def review_delete(request, review_id):
    Review.objects.get(id=review_id).delete()
    return redirect('business_index')

def review_create(request):
    if req.method == 'POST':
        review_form = Review_Form(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user= request.user
            new_review.save()
            return redirect(request.get_full_path())
    context = {'review': review, 'review_create': review_create}
    return render(request, 'business_index.html', context)
    







#=============Review page ==============


 



#============Review page =================







