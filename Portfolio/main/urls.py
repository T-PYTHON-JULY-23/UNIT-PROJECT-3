from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.intro_view, name="intro_view"),
    path("work/", views.work_view, name="work_view"),
    path("about/", views.about_view, name="about_view"),
    path("blog/", views.blog_view, name="blog_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("addmessage/", views.contact_view, name="contact_view"),

]