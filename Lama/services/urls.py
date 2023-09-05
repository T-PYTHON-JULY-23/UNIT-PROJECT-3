from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
        path("update/<service_id>/", views.service_update_view, name="service_update_view"),
        path("add/", views.add_service_view, name="add_service_view"),
        path("allservices/", views.all_services_view, name="all_services_view"),
        path("detail/<service_id>/", views.service_detail_view, name="service_detail_view"),
        path("delete/<service_id>/", views.service_delete_view, name="service_delete_view"),
        path("request/add/<service_id>/", views.add_request_view, name="add_request_view"),
        path("request/", views.user_request_view, name="user_request_view"),
        path("updateRequest/",views.update_request_view,name="update_request_view"),
        path("change_status/<int:request_id>/",views.change_status,name="change_status"),

]