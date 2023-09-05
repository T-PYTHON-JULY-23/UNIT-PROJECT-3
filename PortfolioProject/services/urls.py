from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    path('', views.services_view, name="services_view"),
    path('detail/<service_id>/', views.service_detail_view, name="service_detail_view"),
    path('delete/<service_id>/', views.service_delete_view, name="service_delete_view"),
    path('update/<service_id>/', views.service_update_view, name="service_update_view"),
    path('add/', views.add_service_view, name="add_service_view"),
    path('request/<service_id>/', views.request_service_view, name="request_service_view"),
    path('manageRequest/', views.my_requests_status_view, name="my_requests_status_view"),
    path('updateRequest/<request_id>/', views.update_request_status_view,
         name="update_request_status_view"),
]