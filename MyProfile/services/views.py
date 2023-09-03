from django.shortcuts import render
from django.http import HttpRequest , HttpResponse 

# Create your views here.


def my_services(request:HttpRequest):

    return render(request, 'services/my_services.html')