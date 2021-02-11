from django.urls import path
from . import views


urlpatterns = [
    #home routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('business/', views.business_index, name='business_index'),
    path('business/<int:business_id>/', views.business_detail, name='business_detail'),
    path('review/review_create/<int:business_id>/', views.review_create, name='review_create'),
    path('review/<int:review_id>/edit/', views.review_edit, name='review_edit'),
    path('review/<int:review_id>/delete/', views.review_delete, name='review_delete'),
    path('accounts/signup', views.signup, name='signup'),
    
  
    

    
   
  
   
   
 ]