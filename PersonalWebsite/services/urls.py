from django.urls import path
from . import views

app_name="services"

urlpatterns = [
    path('my_services/',views.services_page_view,name='services_page_view' ),
    path('add_service/', views.add_service_page_view,name='add_service_page_view'),
    path('ubdate_service/<service_id>/',views.ubdate_service_page_view,name='ubdate_service_page_view'),
    path('detail_service/<service_id>/',views.detail_service_page_view,name='detail_service_page_view'),
    path('delet_service/<service_id>/',views.delet_service_view,name='delet_service_view'),
    path('manager/',views.manager_page_view,name='manager_page_view'),
    path('update_status/<request_id>,',views.update_status,name='update_status_view'),
    path('my_request/',views.profil_user_view,name='profil_user_view'),
    path('request/',views.service_request_page,name='service_request_page'),
    path('search_result/', views.search_feature_view, name='search_result_view'),
]