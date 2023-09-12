from django.urls import path
from . import views

app_name = "service"

urlpatterns = [

    path('add/',views.add,name="add_page" ),
    path('all/',views.all_service,name="all_service" ),
    path('detali/<service_id>/', views.detail_serv, name="detail_serv"),
    path('update/<service_id>/', views.update_serv, name="update_serv"),
    path('delete/<service_id>/', views.delete_serv, name="delete_serv"),
    path("request/add/<service_id>/", views.add_request, name="add_request"),
    path("requests/", views.user_serv_request, name="user_serv_request"),
    path("user/request/", views.users_request, name="users_request"),
    path("user/request/update/<request_id>/", views.users_request_update, name="users_request_update"),






   
]