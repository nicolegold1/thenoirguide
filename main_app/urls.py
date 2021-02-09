from django.urls import path
from . import views

urlpatterns = [
    #home routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reviews/', views.reviews_index, name='reviews_index'),
  
    

    
   
  
   
   
 ]