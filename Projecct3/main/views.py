from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Service, ServiceRequest

# Create your views here.
def home_view(request:HttpRequest):
    
    return render(request ,'main/home.html' )


