from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup_user_view, name="signup_user_view"),
    path("login/", views.login_user_view, name="login_user_view"),
    path("logout/", views.logout_user_view, name="logout_user_view")
]