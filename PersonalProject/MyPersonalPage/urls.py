from django.urls import path
from MyPersonalPage import views

app_name = "MyPersonalPage"

urlpatterns = [
    path('MyProjects/', views.MyProjects, name='MyProjects'),
    path('Gallery/', views.Gallery, name='Gallery'),
    path('MyCV/', views.MyCV, name='MyCV'),
    path('AIchatbot/', views.AiChatBot, name='AIchatbot'),
    path('GenderClass/', views.GenderClassification, name='GenderClass'),
    
]