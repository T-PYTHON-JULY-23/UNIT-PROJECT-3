from django.urls import path, include
from. import views
app_name='services'


urlpatterns = [
    path('my_services/',views.my_services,name='my_services.html')
]
