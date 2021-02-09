from django.urls import path, include
from . import views

urlpatterns = [
    #home routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reviews/', views.reviews_index, name='reviews_index'),
    path('reviews/<int:review_id>/' , view.reviews_detail, name='detail'),
    

    
   
  
   
   
 ]