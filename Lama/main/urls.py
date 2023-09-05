from django.urls import path
from . import views


app_name="main"


urlpatterns=[
    path('',views.about_me,name="about_me"),
    path('services/',views.services,name="services"),
]