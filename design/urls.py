from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('career/', views.career, name='career'),
    path('career/career_detail/', views.career_detail, name='career_detail'),
    path('services/', views.services, name='services'),
    path('services/consulting_services/', views.consulting_services, name='consulting_services'),
    
]