from django.urls import path
from . import views

urlpatterns = [
    #home routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('business/', views.business_index, name='business_index'),
    path('business/<int:business_id>/', views.business_detail, name='business_detail'),
    
  
    

    
   
  
   
   
 ]