from django.urls import path
from . import views

app_name= "users"

urlpatterns= [
    path("sign_up/" , views.sign_up , name= "sign_up"),
    path("contact/" , views.contact , name= "contact"),
    path("login/" , views.login_view , name= "login_view"),
    path("logout/" , views.logout_view , name= "logout_view"),



]


