from django.urls import path
from . import views

app_name= "users"

urlpatterns= [
    path("main/sign_up/" , views.sign_up , name= "sign_up"),
    path("main/contact/" , views.contact , name= "contact"),
    path("main/login/" , views.login , name= "login"),


]