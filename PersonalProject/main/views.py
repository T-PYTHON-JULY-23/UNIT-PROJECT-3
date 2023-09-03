from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from MyPersonalPage.models import Post


def home(request: HttpRequest):
    return render(request, 'main/home.html')


def about_view(request: HttpRequest):

    return render(request, "main/home.html")



def dark_view(request:HttpRequest):

    #setting a cookie   
    response = redirect("main:home")
    response.set_cookie("mode", "dark")

    return response


def light_view(request:HttpRequest):
    
    #setting a cookie
    response = redirect("main:home")
    response.set_cookie("mode", "light")

    return response
