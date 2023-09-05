from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import ServerApp , UserRequest, User

def add_server_view(request: HttpRequest):

    if request.user.is_staff:
        if request.method == "POST":
            #adding a book
            new_server = ServerApp(title=request.POST["title"], description=request.POST["description"], image=request.FILES["image"])
            new_server.save()

            return redirect("server_app:all_server_view")
    #else:

    return render(request, 'server_app/add_server.html')


def all_server_view(request: HttpRequest):

    servers = ServerApp.objects.all()
    
    

    return render(request, "server_app/all_server.html", context = {"servers" : servers})


def server_detail_view(request : HttpRequest, server_id):
    
    #to get a single entry in the database
    server = ServerApp.objects.get(id=server_id)


    description = UserRequest.objects.filter(ServerApp=server)

 
    if request.method == "POST" and request.user.is_authenticated:
        description_user = UserRequest(ServerApp=server, user=request.user,description_user=request.POST["description_user"])
        description_user.save()


    return render(request, "server_app/detali.html", {"server" : server,  "description" : description, "UserRequest" : UserRequest})



def server_update_view(request:HttpRequest, server_id):
    
   
        server = ServerApp.objects.get(id=server_id)

        #updating a book
        if request.method == "POST" and request.user.is_staff:
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


def manager_view(request: HttpRequest):
    server =UserRequest.objects.all()
    status=UserRequest.category_choices
    
    return render(request , 'server_app/manager.html', {"server":server,"choices":status})

def manager_edit(request:HttpRequest, request_id):

    user_request=UserRequest.objects.get(id=request_id)

    if  user_request and request.user.is_staff:
        user_request.status =request.POST["status"]
        user_request.save()
        return redirect("server_app:manager_view")
    #else:

    return render(request, 'server_app/manager.html')


def user_request_view(request: HttpRequest):

    add=UserRequest.objects.filter(user=request.user)
    return render(request, 'server_app/profile.html',{"all":add})


def add_requste_view(request: HttpRequest, server_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    
    service=ServerApp.objects.get(id=server_id)

    if not UserRequest.objects.filter(user=request.user, ServerApp=service).exists() and request.POST:
        new_favorite = UserRequest(user=request.user, ServerApp=service)
        new_favorite.save()
        return redirect("server_app:server_detail_view", server_id=server_id)
    return render(request, "server_app/profile.html")