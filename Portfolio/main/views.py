from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index_view(request : HttpRequest):

    return render(request, "main/index.html")


def about_view(request : HttpRequest):
    return render(request, "main/about.html")

def skills_view(request : HttpRequest):
    return render(request, "main/skills.html")

