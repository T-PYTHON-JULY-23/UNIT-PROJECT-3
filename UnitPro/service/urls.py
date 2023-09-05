from django.urls import path
from . import views

app_name ='service'

urlpatterns = [
    path('detail/<service_id>/', views.detail_view, name="detail_view"),
    path('all/', views.all_service_view, name="all_service_view"),  
    path('create/', views.create_view, name="create_view"), 
    path('delete/<service_id>/', views.delete_view, name="delete_view"), 
    path('update/<service_id>/', views.update_view, name="update_view"), 
    path('request/', views.all_request_view, name="all_request_view"), 
    path('request/delete/<service_id>/', views.request_delete_view, name="request_delete_view"),
    path('request/add/<service_id>/', views.add_request_view, name="add_request_view"),
    path('updateStatus/<service_id>/', views.status_update_view, name="status_update_view"),
     
]