from django.shortcuts import render, redirect
from .models import Service,ServiceRequest,User
from django.http import HttpRequest, HttpResponse




def service_view(request: HttpRequest):
    service = Service.objects.all()
    return render(request, 'services/Service.html', {'form': service})


def add_service_view(request: HttpRequest):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")

    if request.method == "POST":
        new_service = Service(title=request.POST["title"], content=request.POST["content"], photo=request.POST["photo"], created_at=request.FILES["created_at"])
        new_service.save()

        return redirect("Services: service")

    return render(request, 'Services/addService.html', {"form": Service})


def service_request_view(request: HttpRequest):

    service = ServiceRequest.objects.all()
    return render(request, 'services/serviceRequest.html', {'form': service})