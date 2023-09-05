from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Service, ServiceRequest

# Create your views here.


def services_view(request: HttpRequest) -> HttpResponse:

    services = Service.objects.all()
    is_empty = services.exists()

    return render(request, 'services/services.html', {'services_list':services, "is_empty": is_empty})



def add_service_view(request: HttpRequest) -> HttpResponse:
    if not request.user.is_staff:
        redirect('accounts:login_view')
    if request.method == "POST":
        if "image" in request.FILES:
            new_service = Service(title=request.POST['title'], description=request.POST['description'], image=request.FILES['image'])
        else:
            new_service = Service(title=request.POST['title'], description=request.POST['description'])
        new_service.save()


    return redirect('services:services_view')


def service_detail_view(request: HttpRequest, service_id) -> HttpResponse:

    service = Service.objects.get(id=service_id)

    return render(request, 'services/service_detail.html', {"service": service})

def service_delete_view(request: HttpRequest, service_id) -> HttpResponse:
    if not request.user.is_staff:
        redirect('accounts:login_view')
    del_service = Service.objects.get(id=service_id)

    del_service.delete()

    return redirect('services:services_view')


def service_update_view(request: HttpRequest, service_id) -> HttpResponse:
    if not request.user.is_staff:
        redirect('accounts:login_view')
        
    upd_service = Service.objects.get(id=service_id)
    if request.method == "POST":
        upd_service.title = request.POST['title']
        upd_service.description = request.POST['description']
        if 'image' in request.FILES:
            upd_service.image = request.FILES['image']

        upd_service.save()

        return redirect('services:service_detail_view', upd_service.id)
    
    return render(request, 'services/update_service.html', {'upd_service':upd_service})

def request_service_view(request: HttpRequest, service_id) -> HttpRequest:

    service = Service.objects.get(id=service_id)

    if not ServiceRequest.objects.filter(user=request.user, service=service).exists():
        new_request = ServiceRequest(user=request.user, service=service, status='pending')
        new_request.save()

        return redirect('accounts:account_view')
    
    return redirect('services:service_detail_view', service_id)


def my_requests_status_view(request: HttpRequest) -> HttpResponse:
    
    if not request.user.is_staff:
        redirect('accounts:login_view')

    all_requests = ServiceRequest.objects.all()

    user_service_requests_done = all_requests.filter(status='done') 
    user_service_requests_pending = all_requests.filter(status='pending') 
    user_service_requests_in_progress = all_requests.filter(status='in_progress') 
    user_service_requests_canceled = all_requests.filter(status='canceled') 

    all_requests = (('Done',user_service_requests_done), ('Pending',user_service_requests_pending), ('In Progress',user_service_requests_in_progress), ('Canceled',user_service_requests_canceled))


    return render(request, 'accounts/manage_request.html', {"requests" : all_requests})

def update_request_status_view(request:HttpRequest, request_id) -> HttpResponse:

    if not request.user.is_staff:
        redirect('accounts:login_view')

    upd_request = ServiceRequest.objects.get(id=request_id)
    if request.method == "POST":
        upd_request.status = request.POST['status']
        upd_request.save()
    
    return redirect('services:my_requests_status_view')
