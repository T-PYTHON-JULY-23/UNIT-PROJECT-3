from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from service.models import Service,ServiceRequest,Comment

# Create your views here.
def home_view(request:HttpRequest):

   services = Service.objects.all()

   return render(request, "main/home_view.html", context = {"services" : services})
