from django.urls import path, include
from. import views
app_name='services'


urlpatterns = [
    path('services_page/',views.my_services,name='service_view'),
    path('my_service_request/',views.my_service_request,name='my_service_request_view'),
    path('my_service_request_staff/',views.my_service_request_staff,name='my_service_request_staff_view'),
    path('change_status/<service_id>/',views.change_status,name='change_status_view'),
    path('add_service/',views.add_service,name='add_service_view'),
    path('update_service/<service_id>/',views.update_service,name='update_service_view'),
    path('service_details/<service_id>/',views.service_details,name='service_details_view'),
    path('book_service/<service_id>/',views.book_service,name='book_service_view'),
    path('delete_service/<service_id>/',views.delete_service,name='delete_service_view')
]
