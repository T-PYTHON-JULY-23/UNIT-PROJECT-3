from django.urls import path
from . import views

app_name = "Services"

urlpatterns = [
    path('Service/', views.service_view, name='service_view'),
    path('addService/', views.add_service_view, name='add_service_view'),
    path('serviceRequest/', views.service_request_view, name='service_request_view'),
    path('userRequests/', views.user_requests_view, name='user_requests_view'),
    
]