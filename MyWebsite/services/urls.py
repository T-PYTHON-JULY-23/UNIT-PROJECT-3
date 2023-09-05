from django.urls import path
from . import views

app_name ="services"

urlpatterns=[
    path("all/", views.all_logo_view, name="all_logo_view"),
    path("add/", views.add_logo_view, name="add_logo_view"),
    path("detail/<logo_id>/", views.logo_detail_view, name="logo_detail_view"),
    path("update/<logo_id>/", views.logo_update_view, name="logo_update_view"),
    path("delete/<logo_id>/", views.logo_delete_view, name="logo_delete_view"),
    path("requests/add/<logo_id>/", views.add_requests_view, name="add_requests_view"),
    path("requests/remove/<logo_id>/", views.remove_requests_view, name="remove_requests_view"),
    path("requests/", views.user_requests_view, name="user_requests_view"),
    

]