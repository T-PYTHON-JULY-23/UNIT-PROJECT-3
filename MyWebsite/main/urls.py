from django.urls import path
from . import views

app_name ="main"

urlpatterns=[
    path("",views.home_view,name="home_view"),
    path("about/",views.about_me,name="about_me"),
    path("podcast/",views.podcast_view,name="podcast_view"),
    
 
]