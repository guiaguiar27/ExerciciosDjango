
from django.contrib import admin
from django.urls import path  
from . import views

urlpatterns = [
    path('login_user', views.login_user, name= "login"), # the name is important for the tags inside of the navbars or other things     
]
