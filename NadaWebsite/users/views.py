from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def sign_up(request : HttpRequest):
    
    if request.method == "POST":
        new_user = User.objects.create_user(first_name=request.POST["first_name"], last_name=request.POST["last_name"], username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], )
        new_user.save()
        return redirect("users:login_view")
    return render(request, "users/sign_up.html")

def contact(request : HttpRequest):
    return render(request, "users/contact.html")

def login_view(request : HttpRequest):
    msg = None
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request, user)         
            return redirect("main:home_view")
        else:
            msg = "Username or password is not correct."
    
    return render(request, "users/login.html", {"msg": msg})


def logout_view(request: HttpRequest):

    logout(request)

    return redirect("users:login_view")