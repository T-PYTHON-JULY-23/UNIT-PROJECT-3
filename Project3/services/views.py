from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import ServerApp, UserRequest , User

# Create your views here.

def services_page(request:HttpRequest):
    services = ServerApp.objects.all()
    return render(request, 'services/services_page.html', context={"services":services})



def add_services_view(request:HttpRequest):

    if request.user.is_staff:
        if request.method == "POST":
            new_server = ServerApp(title=request.POST["title"], description=request.POST["description"], image=request.FILES["image"])
            new_server.save()
           
            return render(request,'services/services.html')
    
    
    return render(request, 'services/add_services.html')



def detaill_services(request:HttpRequest , service_id):

    service = ServerApp.objects.get(id=service_id)

    description = UserRequest.objects.filter(ServerApp=service)


    if request.method == "POST" and request.user.is_authenticated:
        description_user = UserRequest(ServerApp=service , user=request.user, description_user=request.POST["description_user"])
        description_user.save()
    
    return render(request, 'services/detail_services.html', {"servers": service , "description": description, "UserRequest": UserRequest})



def update_services(request:HttpRequest , service_id):

    service = ServerApp.objects.get(id=service_id)


    if request.method == "POST" and request.user.is_staff:
        service.title = request.POST["title"]
        service.description = request.POST["description"]
        if "image" in request.FILES:
            service.image = request.FILES["image"]
        service.save()

        return redirect("services:detaill_services", service_id=service.id)
    return render(request, 'services/update_services.html', {"service": service})



def manager_page(request:HttpRequest):
    services = UserRequest.objects.all()
    status = UserRequest.catgory_choices

    return render(request, 'services/manager_page.html', {"services":services , "status": status})



def manager_only (request:HttpRequest , request_id):
    user_request = UserRequest.objects.get(id=request_id)

    if user_request and request.user.is_staff:
       user_request.status = request.POST["status"]
       user_request.save()
       return redirect("services:manager_only")
   
    return render(request,'services/manager_page.html')

def my_requests(request:HttpRequest):
    add = UserRequest.objects.filter(user=request.user)
    return render(request, 'services/my_requests.html',{"add":add})

def add_request (request: HttpRequest , service_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    
    service= ServerApp.objects.get(id=service_id)

    if not UserRequest.objects.filter(user=request.user , ServerApp=service).exists() and request.POST:
        new = UserRequest(user=request.user , ServerApp=service)
        new.save()
        return redirect("services:detaill_services", service_id=service_id)
    return render(request,"services/my_requests.html")

