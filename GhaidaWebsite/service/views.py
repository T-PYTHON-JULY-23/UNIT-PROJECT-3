from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Service,ServiceRequest

# Create your views here.
def add(request:HttpRequest):
     if not request.user.is_staff:
        return redirect("users:login_user")
     if request.method == "POST":
        #adding a service
        new_service = Service(title=request.POST['title'],description=request.POST['description'],image=request.FILES['image'])
        new_service.save()
        return redirect("service:all_service")
     return render(request,"service/add.html")


def all_service(request: HttpRequest):
        services = Service.objects.all()

        return render(request,"service/all_service.html",{"services":services})


def detail_serv(request: HttpRequest,service_id): 
    
    service=Service.objects.get(id=service_id)
    
    
    return render(request, "service/detail_serv.html",{"service":service})


def update_serv(request: HttpRequest,service_id): 
    if not request.user.is_staff:
        return redirect("users:login_user")
    service=Service.objects.get(id=service_id)
    #updating service
    if request.method == "POST":
        service.title=request.POST['title']
        service.description=request.POST['description']
        if "image" in request.FILES:
         service.image=request.FILES['image']
        service.save()
        return redirect("service:all_service")
        
    
    
    return render(request, "service/update_serv.html",{"service":service})

def delete_serv(request: HttpRequest,service_id): 
    service=Service.objects.get(id=service_id)
    service.delete()
    return redirect("service:all_service")
    

def add_request(request: HttpRequest,service_id):
    
     if not request.user.is_authenticated:
        return redirect("users:login_user")
     
     service=Service.objects.get(id=service_id)
     #if not ServiceRequest.objects.filter(user=request.user, service=service).exists():
     if request.method == "POST":
            new_request = ServiceRequest(user=request.user, service=service,note=request.POST["note"])
            
            new_request.save()
    
     return redirect("service:detail_serv", service_id=service_id)
 
def user_serv_request(request: HttpRequest):
    requests=ServiceRequest.objects.filter(user=request.user)
    return render(request, 'service/requests.html',{"requests":requests})


def users_request(request: HttpRequest):
    requests=ServiceRequest.objects.all()
  
    return render(request, 'service/requset_users.html',{"requests":requests})



def users_request_update(request: HttpRequest, request_id):
    service_request=ServiceRequest.objects.get(id=request_id)
    
    if request.method == "POST":
        service_request.status =request.POST['status']
        service_request.save()
    
    return redirect("service:users_request")



    