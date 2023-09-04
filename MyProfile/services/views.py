from django.shortcuts import render, redirect
from main.models import Service

from django.http import HttpRequest , HttpResponse 


# Create your views here.


def my_services(request:HttpRequest):
    services=Service.objects.all()


    return render(request, 'services/my_services.html',{'services':services})

def service_details(request:HttpRequest,service_id):
    service=Service.objects.get(id=service_id)

    return render(request, 'services/service_detail.html', {'service' : service})

def add_service (request :HttpRequest):


    if not request.user.is_staff:
        return redirect("accounts:login_user_view")

    if request.method == "POST":
        #adding a book
        new_service = Service(title=request.POST["title"], description=request.POST["description"], image=request.FILES["image"])
        new_service.save()

        return redirect("services:service_view")


    return render(request , 'services/add_service.html')


def book_service(request:HttpRequest , service_id):
    print(service_id)
    return redirect("accounts:login_user_view")
    

def update_service(request : HttpRequest, service_id ):

    if not request.user.is_staff:
        return redirect("accounts:login_user_view")
    
    try:
        service = Service.objects.get(id=service_id)

        #updating a book
        if request.method == "POST":
            service.title = request.POST["title"]
            service.description = request.POST["description"] 
            if "image" in request.FILES:
                service.image = request.FILES["image"]
            service.save()

            return redirect("services:service_details_view", service_id=service.id)
    except:
        return render(request, "main/not_found.html")
    
    return render(request, "services/update_service.html", {"service": service})

def delete_service(request : HttpRequest,service_id):
    pass

def my_service_staff(request:HttpRequest):
    pass

def my_service_user(request:HttpRequest):
    pass