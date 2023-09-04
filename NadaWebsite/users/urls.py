from django.urls import path
from . import views

app_name= "users"

urlpatterns= [
    path("sign_up/" , views.sign_up , name= "sign_up"),
    path("contact/" , views.contact , name= "contact"),
    path("login/" , views.login_view , name= "login"),
    path("logout/" , views.logout_user_view , name= "logout_user_view"),



]