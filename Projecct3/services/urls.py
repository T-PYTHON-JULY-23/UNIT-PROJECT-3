from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    path("add_view/", views.add_view, name="add_view"),
    path('services_list/', views.services_list, name='services_list')
    ]