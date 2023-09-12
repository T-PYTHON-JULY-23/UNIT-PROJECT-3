from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Service,ServiceRequest,Comment

# Create your views here.
def detail_view(request:HttpRequest,service_id):

    service = Service.objects.get(id=service_id)
    comments = Comment.objects.filter(service=service)


    if request.method == "POST" and request.user.is_authenticated:
        new_comment = Comment(service=service, user=request.user, content=request.POST["content"], rating=request.POST["rating"])
        new_comment.save()
    return render(request, "service/detail_service.html",{"service":service, "comments" : comments, "Comment" : Comment})


def all_service_view(request:HttpRequest):
   
    services = Service.objects.all()

    return render(request, "service/all_service.html", context = {"services" : services})


def create_view(request:HttpRequest):

    if not request.user.is_staff:
        return redirect("account:login_user_view")
    
    if request.method == "POST":
        new_request = Service(title=request.POST["title"], description=request.POST["description"],image=request.FILES["image"])
        new_request.save()

        return redirect("service:create_view")
    
    return render(request, "service/create_page.html",{"Service":Service})

def delete_view(request: HttpRequest, service_id):

    if not request.user.is_staff:
        return redirect("account:login_user_view")
    #deleting an entry from database
    service = Service.objects.get(id=service_id)
    service.delete()

    return redirect("service:all_service_view")



def update_view(request:HttpRequest, service_id):
    
    if not request.user.is_staff:
        return redirect("account:login_user_view")
    
    try:
       service = Service.objects.get(id=service_id)
       
       if request.method == "POST":
            service.title = request.POST["title"]
            service.description = request.POST["description"]
            service.created_at = request.POST["created_at"]
            if "image" in request.FILES:
                service.image = request.FILES["image"]
            service.save()

            return redirect("service:detail_view", service_id=service_id)
    except:
        return render(request, "main/not_found.html")
    
    service.created_at = service.created_at.strftime("%Y-%m-%d") #2023-05-13 09:02:65

    return render(request, "service/update_service.html", {"service": service})



############
def all_request_view(request:HttpRequest):
    services = ServiceRequest.objects.all()
    choices= ServiceRequest.status_choices
    

    return render(request, "service/all_request.html", context = {"services" : services,"choices":choices})
    
def add_request_view(request:HttpRequest, service_id):
    if not request.user.is_authenticated:
        return redirect("account:login_user_view")
    

    service = Service.objects.get(id=service_id)

    if not ServiceRequest.objects.filter(user=request.user, service=service).exists():
        new_service = ServiceRequest(user=request.user, service=service)
        new_service.save()

    return redirect("service:all_request_view")

def request_delete_view(request: HttpRequest, service_id):
    
    if not request.user.is_authenticated:
        return redirect("account:login_user_view")
    

    service = Service.objects.get(id=service_id)
    user_request = ServiceRequest.objects.filter(user=request.user, service=service).first()

    if user_request:
        user_request.delete()
        

    return redirect("service:all_request_view")
########################


