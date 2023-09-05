from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request:HttpRequest):
    
    return render(request,"main/index.html")

def about_me(request:HttpRequest):
    
    return render(request,"main/about_me.html")

def podcast_view(request:HttpRequest):
    
    return render(request,"main/podcast.html")

