from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home_view(request : HttpRequest) :
    return render(request, "main/homePage.html")

def about_view(request : HttpRequest) :
    return render(request, "main/about.html")
# Create your views here.
