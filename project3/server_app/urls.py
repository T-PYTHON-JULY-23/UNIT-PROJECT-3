from django.urls import path
from . import views

app_name = "server_app"

urlpatterns = [
    path('add/', views.add_server_view,name="add_server_view"),
    path('all/', views.all_server_view,name="all_server_view"),
    path("detail/<server_id>/", views.server_detail_view, name="server_detail_view"),
    path('updeat/<server_id>/', views.server_update_view, name="server_update_view"),
    path('delete/<server_id>/', views.server_delete_view, name="server_delete_view"),
    path('add/request/<server_id>/', views.add_requste_view, name="add_favorite_view"),
    path("request/", views.user_request_view, name="user_favorite_view"),
    path("manager/", views.manager_view, name="manager_view"),
    path("manager/edit/<request_id>",views.manager_edit,name="manager_edit"),



]