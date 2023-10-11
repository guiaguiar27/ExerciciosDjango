
from django.contrib import admin
from django.urls import path  
from . import views

urlpatterns = [
    path('', views.home, name="dashboard"),  
    path('about/', views.about, name = "about"),  
    path('user/', views.user, name="user"),  
    path('service/', views.service, name="service"),  
]
