from django.urls import path
from . import views

urlpatterns = [
    #home routes
    path('', views.home, name='home'),

   
   
    
]