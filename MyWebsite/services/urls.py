from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    path('services/', views.services_view, name="services_view"),
    path('add/', views.add_services_view, name="add_services_view"),
    path('update/<service_id>/', views.update_services_view , name="update_services_view"),
    path('detail/<service_id>/', views.details_services_view , name="details_services_view"),
    path('delete/<service_id>/', views.del_services_view , name="del_services_view"),
    path('sendRequest/', views.send_request_view , name="send_request_view"),
    path('myrequest/', views.request_user_view, name="request_user_view"),
    path('text/', views.text, name="text"),
    path('manage/', views.manage_request_view, name="manage_request_view"),
    path('update_state/<service_request_id>/', views.update_state_view, name="update_state_view")
]