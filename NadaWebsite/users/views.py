from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.

def sign_up(request : HttpRequest):
    return render(request, "users/sign_up.html")

def contact(request : HttpRequest):
    return render(request, "users/contact.html")

def login(request : HttpRequest):
    return render(request, "users/login.html")
