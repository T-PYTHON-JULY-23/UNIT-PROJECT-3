from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Dessert, Order, Confirm


# Create your views here.
def add_dessert_view(request:HttpRequest):
  
    if not request.user.is_staff:
        return redirect("users:login_user_view")
    if request.method == "POST":

        new_dessert = Dessert(title=request.POST["title"],image=request.FILES["image"], ingredients=request.POST["ingredients"],instructions=request.POST["instructions"])

        new_dessert.save()

        return redirect("service:all_dessert_view")
    return render(request, 'main/add_dessert.html')

def update_dessert_view(request:HttpRequest, dessert_id):

    if not request.user.is_staff:
        return redirect("users:login_user_view")
    
    dessert = Dessert.objects.get(id=dessert_id)

    if request.method == "POST":
        dessert.title = request.POST["title"]
        dessert.ingredients = request.POST["ingredients"]
        dessert.instructions = request.POST["instructions"]
        if 'image' in  request.FILES:
            dessert.image=request.FILES["image"]
        dessert.save()

        return redirect("service:dessert_detail_view", dessert_id=dessert.id)

    return render(request,"main/update_dessert.html", {"dessert": dessert})


def delete_dessert_view(request: HttpRequest, dessert_id):

    if not request.user.is_staff:
        return redirect("users:login_user_view")
    #deleting an entry from database
    dessert = Dessert.objects.get(id=dessert_id)
    dessert.delete()

    return redirect("service:all_dessert_view")



def all_dessert_view(request: HttpRequest):

    desserts = Dessert.objects.all()

    return render(request, "main/all_desserts.html", context = {"desserts" : desserts})


def dessert_detail_view(request:HttpRequest, dessert_id):

    dessert = Dessert.objects.get(id=dessert_id)
    dessert.created_at = dessert.created_at.strftime("%b. %Y")
   

    return render(request, "main/dessert_detail.html", {"dessert" : dessert})


def add_order_view(request:HttpRequest,dessert_id):

    if request.method == "POST" and request.user.is_authenticated:
        new_order = Order(dessert=dessert, user=request.user,descrption=request.POST["descrption"])
        new_order.save()

    dessert = Dessert.objects.get(id=dessert_id)
    orders = Order.objects.filter(dessert=dessert)

    return render(request, "main/dessert_detail.html", {"dessert" : dessert, "orders":orders})
        







def confirm_order_view(request: HttpRequest, dessert_id):

    if not request.user.is_authenticated:
        return redirect("users:login_user_view")
    
    dessert = Dessert.objects.get(id=dessert_id)

    if not Confirm.objects.filter(user=request.user, dessert=dessert).exists():
        order_confirm = Confirm(user=request.user, dessert=dessert)
        order_confirm.save()

    return redirect("main:home_view", dessert_id=dessert_id)

def create_order_view(request: HttpRequest, dessert_id):

    if not request.user.is_authenticated:
            return redirect("users:login_user_view") 
       
    dessert = Dessert.objects.get(id=dessert_id)
    order=Order.objects.filter(dessert=dessert)

    is_order=False
    if request.user.is_authenticated:
        is_order = Order.objects.filter(dessert=dessert, user=request.user).exists()
        new_order = is_order(descrption=request.POST["descrption"])

        return redirect("service:all_dessert_view")
        return render(request, 'main/add_dessert.html')