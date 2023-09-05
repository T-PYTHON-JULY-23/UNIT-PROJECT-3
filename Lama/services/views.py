from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Service ,ServiceRequest 
# Create your views here.
 
def service_update_view (request: HttpRequest,service_id):
    try:
        service = Service.objects.get(id=service_id)

        #updating a service
        if request.method == "POST":
            service.title = request.POST["title"]
            service.description = request.POST["description"]
            service.created_at = request.POST["created_at"]
            if "image" in request.FILES:
                service.image = request.FILES["image"]
            service.save()

            return redirect("services:service_update_view", service_id=service.id)
    except:
        return render(request, "main/not_found.html")

    return render(request, "services/update.html", {"service": service})


def add_service_view(request: HttpRequest):

    if request.method == "POST":
        #adding a service
        new_service = Service(title=request.POST["title"], description=request.POST["description"], created_at=request.POST["created_at"], image=request.FILES["image"])
        new_service.save()

        return redirect("services:all_services_view")

    return render(request, 'services/add.html', {"Service": Service})


def all_services_view(request:HttpRequest):
    services = Service.objects.all()

    return render(request, "services/services.html", context = {"services" : services})

def service_detail_view(request:HttpRequest,service_id):
    service = Service.objects.get(id=service_id)

    return render(request, "services/detail.html", {"service" : service})

def service_delete_view(request: HttpRequest, service_id):
    service = Service.objects.get(id=service_id)
    service.delete()

    return redirect("services:all_services_view")

def add_request_view(request: HttpRequest, service_id):
    

    service = Service.objects.get(id=service_id)

    if not ServiceRequest.objects.filter(user=request.user, service=service).exists():
        new_request = ServiceRequest(user=request.user, service=service)
        new_request.save()

    return redirect("services:service_detail_view", service_id=service_id)

def user_request_view(request: HttpRequest):
    user = request.user
    requestservice= ServiceRequest.objects.filter(user=user)
    return render(request, "services/request.html", context= {"requestservice" : requestservice})

def update_request_view(request: HttpRequest):
        
        if request.user.is_staff:  # Ensure the user is an admin
         requestservice = ServiceRequest.objects.all()
        return render(request, "services/update_request.html", {"requestservice": requestservice})
        

def change_status(request:HttpRequest, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')  # Get the new status from the form
        # Update the status of the service request
        service_request.status = new_status
        service_request.save()
        return redirect("services:update_request_view")  # Redirect back to the admin page after updating the status

    # Handle the case where the request method is not POST
    return redirect("services:update_request_view")  # Redirect back to the admin page if the request is not POST
