from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Service , Requests


# Create your views here.


def all_logo_view (request:HttpRequest):
       
     logos = Service.objects.all()

     return render(request, "services/all_logo.html", context = {"logos" : logos})


def add_logo_view (request:HttpRequest):

    if request.method == "POST":
        new_logo = Service(title=request.POST["title"], description=request.POST["description"], image=request.FILES["image"])
        new_logo.save()

        return redirect("services:all_logo_view")

    return render(request, 'services/add_logo.html', {"Service": Service})


def logo_update_view (request:HttpRequest , logo_id):

        logo = Service.objects.get(id=logo_id)

        if request.method == "POST":
            logo.title = request.POST["title"]
            logo.description = request.POST["description"]
            if "image" in request.FILES:
                logo.image = request.FILES["image"]
            logo.save()

            return redirect("services:logo_detail_view", logo_id=logo.id)

        return render(request, "services/update_logo.html", {"logo": logo})
    

def logo_detail_view (request:HttpRequest, logo_id):
    
    logo = Service.objects.get(id=logo_id)
    return render(request, "services/logo_detail.html", {"logo" : logo})


def logo_delete_view (request:HttpRequest, logo_id):
    
    logo = Service.objects.get(id=logo_id)
    logo.delete()

    return redirect("services:all_logo_view")





def add_requests_view (request:HttpRequest, logo_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    

    logo = Service.objects.get(id=logo_id)

    if not Requests.objects.filter(user=request.user, logo=logo).exists():
        new_requests = Requests(user=request.user, logo=logo)
        new_requests.save()

    return redirect("services:logo_detail_view", logo_id=logo_id)
    


def remove_requests_view(request: HttpRequest, logo_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    
    logo = Service.objects.get(id=logo_id)
    user_requests = Requests.objects.filter(user=request.user, logo=logo).first()

    if user_requests:
       user_requests.delete()
        
    return redirect("services:logo_detail_view", logo_id=logo_id)


def user_requests_view(request: HttpRequest):

    return render(request, 'services/requests_page.html')




def manager_page_admin (request:HttpRequest) :
    pass

