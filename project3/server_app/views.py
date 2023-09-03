from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import ServerApp , UserRequest, User

def add_server_view(request: HttpRequest):
    if request.method == "POST":
        #adding a book
        new_server = ServerApp(title=request.POST["title"], description=request.POST["description"], image=request.FILES["image"])
        new_server.save()

        return redirect("server_app:all_server_view")

    return render(request, 'server_app/add_server.html')


def all_server_view(request: HttpRequest):

    servers = ServerApp.objects.all()
    if "search" in request.GET:
        servers = ServerApp.objects.filter(title__contains=request.GET["search"])
    else:
        servers = ServerApp.objects.all()

    return render(request, "server_app/all_server.html", context = {"servers" : servers})


def server_detail_view(request : HttpRequest, server_id):
    
    #to get a single entry in the database
    server = ServerApp.objects.get(id=server_id)

    return render(request, "server_app/detali.html", {"server" : server})



def server_update_view(request:HttpRequest, server_id):
    
   
        server = ServerApp.objects.get(id=server_id)

        #updating a book
        if request.method == "POST":
            server.title = request.POST["title"]
            server.description = request.POST["description"]
            if "image" in request.FILES:
                server.image = request.FILES["image"]
            server.save()

            return redirect("server_app:server_detail_view", server_id=server.id)
        return render(request, "server_app/update_server.html", {"server": server})


def server_delete_view(request: HttpRequest, server_id):
    #deleting an entry from database
    server = ServerApp.objects.get(id=server_id)
    server.delete()

    return redirect("server_app:all_server_view")


def add_favorite_view(request: HttpRequest, server_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    
    service=ServerApp.objects.get(id=server_id)

    if not UserRequest.objects.filter(user=request.user, ServerApp=service).exists() and request.POST:
        new_favorite = UserRequest(user=request.user, ServerApp=service)
        new_favorite.save()
        return redirect("server_app:server_detail_view", server_id=server_id)
    return render(request, "server_app/profile.html")

def user_favorite_view(request: HttpRequest):

    add=UserRequest.objects.filter(user=request.user)
    return render(request, 'server_app/profile.html',{"all":add})

def manager_view(request: HttpRequest):
    status=UserRequest.category_choices
    add=UserRequest.objects.all()
    return render(request, 'server_app/manager.html',{"all":add,"choices":status})


def manager_edit(request:HttpRequest, server_id, user_id):

    status=UserRequest.category_choices
    add=UserRequest.objects.all()
    service=ServerApp.objects.get(id=server_id)
    user=User.objects.get(id=user_id)

    if not UserRequest.objects.filter(user=user, ServerApp=service).exists():
        new_favorite = UserRequest(user=user, ServerApp=service,status=request.POST["status"])
        new_favorite.save()
        return redirect("server_app:manager_view")
    return render(request, 'server_app/manager.html',{"all":add,"choices":status})


