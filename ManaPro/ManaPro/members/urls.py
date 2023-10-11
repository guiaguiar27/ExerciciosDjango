
from django.contrib import admin
from django.urls import path  
from . import views

urlpatterns = [
    path('', views.login_user, name= ""), # the name is important for the tags inside of the navbars or other things     
]
