from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from services.models import Service, ServiceRequest
# Create your views here.


def account_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        user = request.user
        user_service_requests = ServiceRequest.objects.filter(user=user)

        if user.is_staff:
            return redirect('services:my_requests_status_view')
        else:
            return render(request, 'accounts/account.html', {'user': user, "requests":user_service_requests})
    return redirect('accounts:login_view')


def login_view(request: HttpRequest) -> HttpResponse:
    msg = None
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)

            if request.user.is_staff:
                return redirect('services:my_requests_status_view')
            else:
                return redirect('accounts:account_view')

        else:
            msg = 'Opps you may entered the user name or the password '.capitalize()

    return render(request, 'accounts/login.html', {'msg': msg})


def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'],
                                        first_name=request.POST['first_name'], last_name=request.POST['last_name'])
        user.save()
        return redirect('accounts:login_view')
    else:
        return render(request, 'accounts/register.html')


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("accounts:login_view")

    