from django.urls import path,include
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('about',views.about_view,name='about_view'),
  
]