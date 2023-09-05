from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Service, ServiceRequest
# Create your views here.


def services_view(request:HttpRequest):
    services = Service.objects.all()
    return render(request,"services.html",{"services":services})


def add_services_view(request:HttpRequest):
    if not request.user.is_staff:
        return redirect("main:base_view")
    
    if request.method == "POST":
        new_service = Service(title=request.POST["title"], description=request.POST["description"], image=request.FILES["image"])
        new_service.save()
        return redirect("services:services_view")

    return render(request,"add_services.html")



def update_services_view(request:HttpRequest, service_id):
    if not request.user.is_staff:
        return redirect("main:base_view")
    


    service = Service.objects.get(id=service_id)
    if request.method == "POST":
        service.title=request.POST["title"]
        service.description= request.POST["description"]
        if "image" in request.FILES:
            service.image=request.FILES["image"]
        service.save()
        return redirect("services:details_services_view", service_id=service.id)
    return render(request, "update_services.html", {"service":service})



def details_services_view(request:HttpRequest, service_id):
    service = Service.objects.get(id=service_id)
    request_service = ServiceRequest.objects.filter(service=service)
    if request.method == "POST":
        new_requset = ServiceRequest(service=service, user=request.user)
        new_requset.save()
        return redirect("services:send_request_view")
    return render(request, "detail_services.html", {"service":service})


def del_services_view(request:HttpRequest, service_id):
    if not request.user.is_staff:
        return redirect("main:base_view")
    service = Service.objects.get(id=service_id)
    service.delete()
    return redirect("services:services_view")


# def request_services_view(request:HttpRequest, service_id):

def send_request_view(request:HttpRequest):
    if not request.user.is_authenticated:
        return redirect("main:base_view")
    return render(request, "send_request.html")


def request_user_view(request:HttpRequest):
    if not request.user.is_authenticated:
        return redirect("main:base_view")

    new_request = ServiceRequest.objects.filter(user=request.user)
    return render(request,"my_request.html",{"serviceRequests":new_request})


def text(request:HttpRequest):
    return render(request,"text.html")


def manage_request_view(request:HttpRequest):
    if not request.user.is_staff:
        return redirect("main:base_view")
    
    new_request = ServiceRequest.objects.all()
    return render(request,"manage_requests.html", {"serviceRequests":new_request})







def update_state_view(request:HttpRequest,service_request_id):
    if not request.user.is_staff:
        return redirect("main:base_view")
    

    new_request_id = ServiceRequest.objects.get(id=service_request_id)
    if request.method == "POST":
        new_request_id.state = request.POST["state"]
        new_request_id.save()
        return redirect("services:manage_request_view")
    return render(request, "update_state.html",{"new_request":new_request_id})


