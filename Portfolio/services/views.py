from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Service,ServiceRequest




def add_service_view(request: HttpRequest):

    if not request.user.is_staff:
        return redirect("main:about_view")
    if request.method == "POST":
        new_service = Service(title=request.POST["title"], description=request.POST["description"], image=request.FILES["image"])
        new_service.save()

        return redirect("services:service_view")

    return render(request, 'services/add_service.html', {"Service": Service})



def service_view(request: HttpRequest):
     
     service = Service.objects.all()

     return render(request, "services/service.html", {"services" : service})

def service_update_view(request:HttpRequest, service_id):
         
        if not request.user.is_staff:
            return redirect("main:about_view")
   
        service = Service.objects.get(id = service_id)

        if request.method == "POST":
            service.title = request.POST["title"]
            service.description = request.POST["description"]
            if "image" in request.FILES:
                service.image = request.FILES["image"]
            service.save()

            return redirect("services:service_detail_view", service_id = service.id)
        


    

        return render(request, "services/update.html",{"service": service})

def service_detail_view(request : HttpRequest, service_id):
    
    service = Service.objects.get(id=service_id)
    request_service = ServiceRequest.objects.filter(service = service)
    if request.method == "POST":
        new_request = ServiceRequest(service=service, user = request.user)
        new_request.save()

        return redirect("services:service_view")

    return render(request, "services/details.html", {"service" : service})


def service_delete_view(request : HttpRequest , service_id):

    service = Service.objects.get(id = service_id)
    service.delete()

    return redirect("services:service_view")


def add_request_view(request: HttpRequest,service_id):

    service = Service.objects.get(id=service_id)
    request_service = ServiceRequest.objects.filter(service = service)
    if request.method == "POST":
        new_request = ServiceRequest(service=service, user = request.user)
        new_request.save()

        return redirect("services:show_request_view")
    return render(request, 'services/myrequest.html', {"servicereq" : new_request})

def show_request_view(request: HttpRequest):
    

    new_request = ServiceRequest.objects.filter(user=request.user )

    return render(request, 'services/myrequest.html', {"servicereq" : new_request})

def manage_request(request:HttpRequest):
    if not request.user.is_staff:
        return redirect("main:about_view")
    
    new_request = ServiceRequest.objects.all()
    return render(request,"services/manage.html" , {"allreq" : new_request})

def update_status(request:HttpRequest,servicerequest_id):
    if not request.user.is_staff:
        return redirect("main:about_view")
    
    servicerequest = ServiceRequest.objects.get(id = servicerequest_id)
    if request.method == "POST":
        servicerequest.status = request.POST["status"]
        servicerequest.save()

        return redirect("services:manage_request")
    return render(request , "services/update_status.html",{"servicerequest" : servicerequest})
