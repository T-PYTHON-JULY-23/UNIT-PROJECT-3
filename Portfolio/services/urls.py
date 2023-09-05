from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    path("add/", views.add_view, name="add_view"),
    path("update/<service_id>/", views.update_view, name="update_view"),
    path("detail/<service_id>/", views.detail_view, name="detail_view"),
    path("display/", views.display_view, name="display_view"),
    path("my_requests/", views.my_requests_view, name="my_requests_view"),
    path("manage_requests/", views.manage_requests_view, name="manage_requests_view"),
    path("delete/<service_id>/", views.delete_view, name="delete_view"),
    path("status/<request_id>/", views.status_update_view, name="status_update_view"),
]