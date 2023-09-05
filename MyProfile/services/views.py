from django.shortcuts import render, redirect
from main.models import Service,ServiceRequest

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
    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    
    service=Service.objects.get(id=service_id)
    serv=ServiceRequest.objects.filter(user=request.user,service=service)
    print(len(serv))

    new_service_request=ServiceRequest(service=service, user=request.user )
    new_service_request.save()
    return redirect("services:my_service_request_view")
    

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

    if not request.user.is_staff:
        service_request=ServiceRequest.objects.get(id=service_id)
        service_request.delete()
        return redirect('services:my_service_request_view')

def my_service_request(request:HttpRequest):
    
    return render(request,'services/my_service_request.html')

def my_service_request_staff(request : HttpRequest):

    all_service_requests=ServiceRequest.objects.all()

    return render(request,'services/my_serivce_request_staff.html',context={'all_service_request':all_service_requests,'ServiceRequest':ServiceRequest})


def change_status(request :HttpRequest, service_id ):


    if request.user.is_staff and request.method=='POST' :

        service_request=ServiceRequest.objects.get(id=service_id)
        service_request.status = request.POST['status']
        service_request.save()
        
    return redirect('services:my_service_request_staff_view')

def delete_service_staff(request:HttpRequest,service_id):

    if  request.user.is_staff:
        service=Service.objects.get(id=service_id)
        service.delete()
        return redirect('services:my_service_request_view')
