from django.shortcuts import render , redirect,get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Shirt, Comment, Product,ChildrenShirt

# Create your views here.  
def profile_view(request : HttpRequest):

  
    return render(request, "main/profile.html")

def about_view(request : HttpRequest):

  
    return render(request, "main/about.html")

def education_view(request : HttpRequest):

  
    return render(request, "main/education.html")

def home_view(request : HttpRequest):
    main = Shirt.objects.all()
    child_shirt = ChildrenShirt.objects.all()
    return render(request, "main/home.html", context = {"main" : main ,"child_shirt" : child_shirt})

def add_shirt_view(request: HttpRequest):
    if request.method == "POST":
        new_shirt = Shirt(title=request.POST["title"],  price =request.POST["price"],image=request.FILES["image"])
        new_shirt.save()
        return redirect("main:shirts_view")
    return render(request, 'main/add_shirt.html')

def add_childrenShirt_view(request: HttpRequest):
    if request.method == "POST":
        new_shirt = ChildrenShirt(title=request.POST["title"],  price =request.POST["price"],image=request.FILES["image"])
        new_shirt.save()
        return redirect("main:home_view")
    return render(request, 'main/add_childrenShirt.html')



def shirts_view(request: HttpRequest):
    main = Shirt.objects.all()
    child_shirt = ChildrenShirt.objects.all()

    return render(request, "main/shirts.html", context = {"main" : main ,"child_shirt" : child_shirt})


def shirt_detail_view(request : HttpRequest, shirt_id):
    try:
        shirt = Shirt.objects.get(id=shirt_id)
        comments = Comment.objects.filter(shirt=shirt)
        
        is_product = False

        if request.user.is_authenticated:
            is_product = Product.objects.filter(shirt=shirt, user=request.user).exists()

        if request.method == "POST" and request.user.is_authenticated :
            new_comment = Comment(shirt=shirt, user=request.user, content=request.POST["content"], rating=request.POST["rating"])
            new_comment.save()
    except:
        return render(request, "main/not_found.html")

    return render(request, "main/shirt_detail.html", {"shirt" : shirt , "comments" : comments, "Comment" : Comment, "is_product" : is_product})


def child_shirt_detail_view(request : HttpRequest, child_shirt_id):
    try:
        child_shirt = ChildrenShirt.objects.get(id=child_shirt_id)
        comments = Comment.objects.filter(child_shirt=child_shirt)
        
        is_product = False

        if request.user.is_authenticated:
            is_product = Product.objects.filter(child_shirt=child_shirt, user=request.user).exists()

        if request.method == "POST" and request.user.is_authenticated :
            new_comment = Comment(child_shirt=child_shirt, user=request.user, content=request.POST["content"], rating=request.POST["rating"])
            new_comment.save()
    except:
        return render(request, "main/not_found.html")

    return render(request, "main/child_shirt_detail.html", {"child_shirt" : child_shirt , "comments" : comments, "Comment" : Comment, "is_product" : is_product})


def shirt_update_view(request:HttpRequest, shirt_id):
    try:
        shirt = Shirt.objects.get(id=shirt_id)

        if request.method == "POST":
            shirt.title = request.POST["title"]
            shirt.price = request.POST["price"]
            if "image" in request.FILES:
                shirt.image = request.FILES["image"]
            shirt.save()
            return redirect("main:shirt_detail_view", shirt_id=shirt.id)
    except:
        return render(request, "main/not_found.html")
    
    
    return render(request, "main/update_shirt.html", {"shirt": shirt})

def child_shirt_update_view(request:HttpRequest, child_shirt_id):
    try:
        child_shirt = ChildrenShirt.objects.get(id=child_shirt_id)

        if request.method == "POST":
            child_shirt.title = request.POST["title"]
            child_shirt.price = request.POST["price"]
            if "image" in request.FILES:
                child_shirt.image = request.FILES["image"]
            child_shirt.save()
            return redirect("main:child_shirt_detail_view", shirt_id=child_shirt.id)
    except:
        return render(request, "main/not_found.html")
    
    
    return render(request, "main/update_child_shirt.html", {"child_shirt": child_shirt})


def shirt_delete_view(request: HttpRequest, shirt_id):
    try:
        shirt = Shirt.objects.get(id=shirt_id)
        shirt.delete()
        return redirect("main:shirts_view")
    except:
        return render(request, "main/not_found.html")
    
def child_shirt_delete_view(request: HttpRequest, child_shirt_id):
    try:
        child_shirt = ChildrenShirt.objects.get(id=child_shirt_id)
        child_shirt.delete()
        return redirect("main:shirts_view")
    except:
        return render(request, "main/not_found.html")


def shirts_search_view(request: HttpRequest):

    if "search" in request.GET:
        main = Shirt.objects.filter(title__contains=request.GET["search"])
        child_shirt= ChildrenShirt.objects.filter(title__contains=request.GET["search"])
    else:
        main = Shirt.objects.all()
        child_shirt=ChildrenShirt.objects.all()

    return render(request, 'main/search.html', {"main" : main, "child_shirt":child_shirt})

def add_product_view(request:HttpRequest,shirt_id):

    if not request.user.is_authenticated :
        return redirect("accounts:login_user_view")
    
    shirt = Shirt.objects.get(id=shirt_id)
    
    if not Product.objects.filter(user=request.user, shirt=shirt).exists() :
        new_product = Product(user=request.user, shirt=shirt)
        new_product.save()
    return redirect("main:user_product_view")

def add_child_shirt_product_view(request:HttpRequest,child_shirt_id):

    if not request.user.is_authenticated :
        return redirect("accounts:login_user_view")
    
    child_shirt = ChildrenShirt.objects.get(id=child_shirt_id)
    
    if not Product.objects.filter(user=request.user, child_shirt=child_shirt).exists() :
        new_product = Product(user=request.user, child_shirt=child_shirt)
        new_product.save()
    return redirect("main:user_product_view", child_shirt_id=child_shirt_id)

def remove_child_shirt_product_view(request: HttpRequest, child_shirt_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    

    child_shirt = ChildrenShirt.objects.get(id=child_shirt_id)
    user_product = Product.objects.filter(user=request.user, child_shirt=child_shirt).first()

    if user_product:
        user_product.delete()
        

    return redirect("main:user_product_view")

def remove_product_view(request: HttpRequest, product_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    

    user_product = Product.objects.get(id=product_id)

    if user_product:
        user_product.delete()
        

    return redirect("main:user_product_view")

def user_product_view(request: HttpRequest):

    return render(request, 'main/product.html')
    
    
def checkout_view(request: HttpRequest):

    return render(request, 'main/checkout.html')
    