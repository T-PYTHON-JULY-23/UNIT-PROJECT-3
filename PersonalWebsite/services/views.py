from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Service,ServiceRequest

from django.contrib.auth.decorators import login_required


# Create your views here.

def services_page_view(request:HttpRequest):
    all_service = Service.objects.all().order_by('title')

    return render(request, 'services/services_page.html', {'all_service':all_service})


def add_service_page_view(request:HttpRequest):
   

    if not request.user.is_staff:
        return redirect("accounts:login_page_view")
        

    if request.method=='POST':
        new_service = Service(title = request.POST['title'],description=request.POST['description'],category=request.POST['category'],image=request.FILES['image'])
        new_service.save()
        return redirect ('services:services_page_view')

    return render(request, 'services/add_service_page.html', {'add_service': Service.category_choices})





def detail_service_page_view(request:HttpRequest,service_id):
    detail_service = Service.objects.get(id=service_id)
    service_request = ServiceRequest.objects.filter(service=detail_service)

    if request.method == "POST":
        new_service_request = ServiceRequest(service=detail_service, user=request.user, pro_discription=request.POST["pro_discription"])
        new_service_request.save()
        return render ( request,'services/submit_request_page.html')

    return render(request,'services/detail_service_page.html', {"detail_service":detail_service, "service":service_request,  "service_request":ServiceRequest,})



def ubdate_service_page_view(request:HttpRequest,service_id):
    if not request.user.is_staff:
        return redirect("accounts:login_page_view")
       
    try: 
        service_ubdate = Service.objects.get(id=service_id)

        if request.method=='POST':
            service_ubdate.title = request.POST['title']
            service_ubdate.description = request.POST['description']
            service_ubdate.category = request.POST['category']

            if 'image' in request.FILES:
                service_ubdate.image=request.FILES['image']
            service_ubdate.save()

            return redirect('services:detail_service_page_view', service_id=service_ubdate.id)
    except:
        return render(request,'services/not_found.html')
    
    return render(request,'services/ubdate_service_page.html',{'service_ubdate':service_ubdate})



def delet_service_view(request:HttpRequest, service_id):
    if not request.user.is_staff:
        return redirect("accounts:login_user_view")
    

    service_delet = Service.objects.get(id=service_id)
    service_delet.delete()

    return redirect('services:services_page_view')



def manager_page_view(request:HttpRequest):
    if not request.user.is_staff:
        return render (request,"services/not_authorrized.html")
     

    service_requests=ServiceRequest.objects.all()
    return render(request,'services/manager_page.html',{"service_requests":service_requests})


def update_status(request:HttpRequest,request_id):
        if not request.user.is_staff:
            return redirect("accounts:login_page_view")
        
        update_status_request = ServiceRequest.objects.get(id=request_id)

        if request.method=='POST':
            update_status_request.status = request.POST['status']
            update_status_request.save()

        return redirect('services:manager_page_view')
    

def profil_user_view(request:HttpRequest):
    user_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request,'services/request_user_page.html',{'user_requests':user_requests})



def service_request_page(request:HttpRequest):
    return render(request,'services/service_request_page.html')



def search_feature_view(request:HttpRequest):
    
    if 'search' in request.GET:
        service= Service.objects.filter(title__contains=request.GET['search'])
    else:
        service=Service.objects.all()

    return render(request, 'services/search_result.html', {'service':service}) 


    



  
    










