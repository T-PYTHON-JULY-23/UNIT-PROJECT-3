from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    path("servicesP/",views.services_page, name ="services_page"),
    path("add/",views.add_services_view, name= "add_services_view"),
    path("detail/<service_id>/",views.detaill_services, name ="detaill_services"),
    path('update/<service_id>/',views.update_services, name="update_services"),
    path("manager/", views.manager_page, name ="manager_page_view"),
    path('manager/only/<request_id>/', views.manager_only, name ="manager_only"),
    path('add/request/<service_id>/',views.add_request, name="add_request"),
    path("myrequests/",views.my_requests, name="my_requests"),


    
]