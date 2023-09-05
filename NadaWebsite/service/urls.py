from django.urls import path
from . import views

app_name= "service"

urlpatterns= [
    path("add/" , views.add_Service , name= "add_Service"),
    path("all/" , views.all_services_view , name= "all_services_view"),
    path('detali/<service_id>/', views.service_detail, name="service_detail"),
    path("update/<service_id>/", views.service_update_view, name="service_update_view"),
    path("delete/<service_id>/", views.service_delete_view, name="service_delete_view"),
    path("request/add/<service_id>/", views.add_request, name="add_request"),
    path("requests/", views.user_service_request, name="user_service_request"),
    path("user/request/", views.users_request, name="users_request"),
    path("user/request/update/<request_id>/", views.users_request_update, name="users_request_update"),
]

