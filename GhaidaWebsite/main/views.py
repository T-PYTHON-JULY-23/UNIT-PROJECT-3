from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def home(request:HttpRequest):
    return render(request,"main/home.html")
def about(request:HttpRequest):
    return render(request,"main/about.html")
def projects(request:HttpRequest):
    return render(request,"main/projects.html")
