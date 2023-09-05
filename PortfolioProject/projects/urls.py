from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_view, name="project_view")
]