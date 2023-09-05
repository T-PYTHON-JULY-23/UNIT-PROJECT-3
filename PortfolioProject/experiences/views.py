from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from services.models import Service, ServiceRequest

# Create your views here.

def experience_view(request: HttpRequest) -> HttpResponse:
    
    return render(request, 'experience/experience.html')