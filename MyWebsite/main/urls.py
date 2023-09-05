from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('home/', views.home_view, name="home_view"),
    path('', views.base_view, name="base_view"),
    
]