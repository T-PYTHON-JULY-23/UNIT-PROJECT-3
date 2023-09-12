from django.urls import path
from . import views

app_name= 'main'

urlpatterns = [
    path('',views.home_page_view, name='home_page_view'),
    path('about_me/',views.about_page_view,name='about_page_view'),
    path('contact_me/',views.contact_page_view,name='contact_page_view')
]
