from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest

# Create your views here.

def home_view(request:HttpRequest):
    return render(request,'main/home.html')

def about_view(request:HttpRequest):
    return render(request,'main/about.html')

