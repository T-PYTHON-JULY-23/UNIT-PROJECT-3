from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Service, ServiceRequest


# Create your views here.


def add_view(request: HttpRequest):
    if request.method == 'POST':
        post = Service(title=request.POST["title"],  description=request.POST["description"])
        post.save()
        return redirect('main:services_list')
    return render(request, 'services/add_services.html')




def services_list(request:HttpRequest):
    services = Service.objects.all()
    return render(request, 'main/all_service.html', {'services': services})