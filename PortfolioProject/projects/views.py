from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Project

# Create your views here.


def project_view(request: HttpRequest) -> HttpResponse:

    projects = Project.objects.all()
    
    if request.method == "POST":
        new_project = Project()

    return render(request, 'projects/projects.html', {"projects": projects})
