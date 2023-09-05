from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.

def about_me (request):

    return render(request , 'main/aboutme.html')

def services (request):

    return render(request , 'main/services.html')


