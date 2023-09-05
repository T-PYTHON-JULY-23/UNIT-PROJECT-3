from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('',views.home_view , name = 'home_view'),
    path('ach/',views.achievement_view , name ='achievement_view'),
    path('moments',views.moments_view, name= 'moments_view'),
]
