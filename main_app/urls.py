from django.urls import path
from . import views

urlpatterns = [
    #home routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('business/', views.business_index, name='index')
    # path('reviews/<int:reviews_id>/', views.reviews_detail, name='detail'),
    
  
    

    
   
  
   
   
 ]