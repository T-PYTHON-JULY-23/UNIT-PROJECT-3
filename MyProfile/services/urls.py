from django.urls import path, include
from. import views
app_name='services'


urlpatterns = [
    path('services_page/',views.my_services,name='service_view'),
    path('add_service/',views.add_service,name='add_service_view'),
    path('update_service/<service_id>/',views.update_service,name='update_service_view'),
    path('service_details/<service_id>/',views.service_details,name='service_details_view'),
    path('book_service/<service_id>/',views.book_service,name='book_service_view')
]
