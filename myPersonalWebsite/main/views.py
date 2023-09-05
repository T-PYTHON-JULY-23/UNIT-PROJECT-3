from django.http import HttpRequest
from django.shortcuts import render,redirect, resolve_url

from .models import Service, ServiceRequest

# Create your views here.
def home_view(request: HttpRequest):
    services = Service.objects.all().order_by("-publish_date")[0:3]
    return render(request, "main/home.html", context = {"services" : services})

def add_service_view(request: HttpRequest):
    try:
        msg= None
        if not request.user.is_staff:
            return redirect("accounts:login_user_view")

        if request.method == "POST":
            new_service = Service(title=request.POST["title"], description=request.POST["description"],image=request.FILES["image"])
            new_service.save()
            msg='Service added'
            url = resolve_url("main:services_view") + "?msg=" + msg
            return redirect(url)

        return render(request, 'main/add_service.html')
    except: 
        msg='Something went wrong..'
        return redirect("main:services_view")
    
def services_view(request: HttpRequest):
    services = Service.objects.all()
    return render(request, "main/services.html", context = {"services" : services})

def service_detail_view(request: HttpRequest,service_id):
    try:
        msg=None
        service = Service.objects.get(id=service_id)
        serviceRequest = ServiceRequest.objects.filter(service=service)
        if request.user.is_authenticated:
            is_serviceRequest = ServiceRequest.objects.filter(service=service, user=request.user).exists()  
        if request.method == "POST":
            if request.user.is_authenticated and not is_serviceRequest:
                new_service = ServiceRequest(service=service, user=request.user, status=request.POST["status"])
                new_service.save()
                msg="Request sent!"
            else:
                msg='Request has already been sent!'

        return render(request, "main/service_detail.html", context = {"service" : service ,'msg':msg})
    except:
         msg="Something went wrong"
         return redirect("main:main/home.html")

def delete_view(request: HttpRequest,service_id):
    try:
        if not request.user.is_staff:
            return redirect("accounts:login_user_view")
        
        service = Service.objects.get(id=service_id)
        service.delete()
        msg='Service Deleted'
        url = resolve_url("main:services_view") + "?msg=" + msg
        return redirect(url)
    except:
        return redirect("main:main/home.html")
    
def update_service_view(request: HttpRequest,service_id):
    try:
        msg= None
        if not request.user.is_staff:
            return redirect("accounts:login_user_view")

        service = Service.objects.get(id=service_id)
        if request.method == "POST":
            service.title = request.POST["title"]
            service.description = request.POST["description"]
            if "image" in request.FILES:
                service.image = request.FILES["image"]
            service.save()
            msg='Service updated'
            url = resolve_url("main:services_view") + "?msg=" + msg
            return redirect(url,service_id =service.id)

        return render(request, 'main/update_service.html',{"service" : service})
    except: 
        return redirect("main:main/services.htm")
    
def services_request_view(request: HttpRequest):
    services_request = ServiceRequest.objects.all()
    return render(request, "main/services_request.html", context = {"services_request" : services_request})

def update_request_view(request: HttpRequest,service_request_id):
    try:
        msg= None
        if not request.user.is_staff:
            return redirect("accounts:login_user_view")
        services_request = ServiceRequest.objects.get(id=service_request_id)
        services_request.status = request.POST["status"]
        services_request.save()
        msg='Status updated'
        url = resolve_url("main:services_request_view") + "?msg=" + msg
        return redirect(url)
    except: 
        return redirect("main:main/services.htm")
    
def user_request_view(request: HttpRequest):

    return render(request, 'main/user_request.html')

def delete_request_view(request: HttpRequest,servicerequest_id):
    try:
        if not request.user.is_authenticated:
            return redirect("accounts:login_user_view")
        
        services_request = ServiceRequest.objects.get(id=servicerequest_id)
        services_request.delete()
        msg='Request Deleted'
        url = resolve_url("main:user_request_view") + "?msg=" + msg
        return redirect(url)
    except:
        return redirect("main:main/home.html")