from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
# from django.contrib.auth import authenticate, login, logout

# # Create your views here.


# def login_view(request:HttpRequest):
#     if request.POST == 'POST':
#         user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
#         if user:
#             login(request,user)
#             return redirect("accounts:logout_view")
#     return render(request,"login.html")

# # def registr_view(request:HttpRequest):
# #     new_user = User(user=request.user, first_name=request.first_name)
# #     return render(request,"login.html")

# def logout_view(request:HttpRequest):
#     return render(request,"logout.html")


def home_view(requset:HttpRequest):
    return render(requset,"home.html")


def base_view(requset:HttpRequest):
    return render(requset,"base.html")