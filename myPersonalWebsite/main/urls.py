from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("service/add", views.add_service_view, name="add_service_view"),
    path("services", views.services_view, name="services_view"),
    path("service/<service_id>/", views.service_detail_view, name="service_detail_view"),
    path("delete/<service_id>/", views.delete_view, name="delete_view"),
    path("update/<service_id>/", views.update_service_view, name="update_service_view"),
    path("services/request", views.services_request_view, name="services_request_view"),
    path("services/update/<service_request_id>", views.update_request_view, name="update_request_view"),
    path("services/request/view", views.user_request_view, name="user_request_view"),
    path("services/request/delete/<servicerequest_id>", views.delete_request_view, name="delete_request_view"),
]