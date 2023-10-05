from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request): 
    string_return = 'Home'
    return   HttpResponse(string_return)
def about(request): 
    string_return = 'About' 
    return HttpResponse(string_return)
def user(request):
    string_return = 'User' 
    return HttpResponse(string_return) 
def service(request):
    string_return = 'Services' 
    return HttpResponse(string_return) 
