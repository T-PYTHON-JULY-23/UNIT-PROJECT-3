from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_view(request:HttpRequest):
    msg = None
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request,user)
            return redirect("main:base_view")
        else:
            msg="Invalid username and password combination"
    return render(request,"login.html",{"msg":msg})


def registr_view(request:HttpRequest):
    if request.method == "POST":
        new_user = User.objects.create_user(first_name=request.POST["first_name"], last_name=request.POST["last_name"], username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], )
        new_user.save()
        return redirect("accounts:login_view")
    return render(request,"register.html")

def logout_view(request:HttpRequest):
    logout(request)
    return redirect("main:base_view")
def profile_view(request:HttpRequest):
    
    return render(request,"profile.html")
