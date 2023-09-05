from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from services.models import Service

# Create your views here.


def home_view(request: HttpRequest) -> HttpResponse:
    myServices = Service.objects.all()[0:3]
    return render(request, 'main/home.html', {'services' : myServices})

