from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

    path('',views.home,name="home_page" ),
    path('about/',views.about,name="about_page" ),
    path('projects/',views.projects,name="projects_page" ),

   
]