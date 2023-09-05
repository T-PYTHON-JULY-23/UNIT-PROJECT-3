from django.urls import path
from . import views

app_name = 'experiences'

urlpatterns = [
    path('', views.experience_view, name="experience_view")
]