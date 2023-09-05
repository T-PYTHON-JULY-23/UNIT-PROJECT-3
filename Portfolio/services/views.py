from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Service, ServiceRequest


def add_view(request: HttpRequest):
    if not request.user.is_staff:
        return redirect("accounts:login_user_view")

    if request.method == "POST":
        #adding a book
        new_service = Service(title=request.POST["title"],icon=request.POST["icon"] ,description=request.POST["description"],content=request.POST["content"], publish_date=request.POST["publish_date"], image=request.FILES["image"])
        new_service.save()

        return redirect("services:display_view")

    return render(request, 'services/add.html', {"Service": Service})



def detail_view(request : HttpRequest, service_id):
    service = Service.objects.get(id=service_id)

    if request.method == "POST" and request.user.is_authenticated:
        new_request = ServiceRequest(service=service, user=request.user, status="pending")
        new_request.save()

    return render(request, "services/detail.html", {"service" : service})



def delete_view(request : HttpRequest, service_id):
    
    if not request.user.is_staff:
        return redirect("accounts:login_user_view")
    #deleting an entry from database
    service = Service.objects.get(id=service_id)
    service.delete()

    return redirect("services:display_view")


def update_view(request:HttpRequest, service_id):
      
      if not request.user.is_staff:
        return redirect("accounts:login_user_view")
      try:
        service = Service.objects.get(id=service_id)

        if request.method == "POST":
            service.title = request.POST["title"]
            service.description = request.POST["description"]
            service.content = request.POST["content"]
            service.publish_date = request.POST["publish_date"]
            if "image" in request.FILES:
                service.image = request.FILES["image"]
            service.save()

            return redirect("services:detail_view", service_id=service.id)
      except:
        return render(request, "main/not_found.html")
    
      return render(request, "services/update.html", {"service": service})


def display_view(request: HttpRequest):
   
 services = Service.objects.all()

 return render(request, "services/display.html", context = {"services" : services})



def my_requests_view(request: HttpRequest):
 if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")

 service_request = ServiceRequest.objects.filter(user=request.user)

 return render(request,"services/my_requests.html",{"requests" : service_request})




def manage_requests_view(request: HttpRequest):
 service_request = ServiceRequest.objects.all()
 

 return render(request,"services/manage_requests.html",{"requests" : service_request, "category_status": ServiceRequest.category_status})



def status_update_view(request: HttpRequest,request_id):
 if not request.user.is_staff:
        return redirect("accounts:login_user_view")
 
 update_status = ServiceRequest.objects.get(id=request_id)

 if request.method == "POST":
        update_status.status = request.POST["status"]
        update_status.save()

 return redirect("services:display_view")




