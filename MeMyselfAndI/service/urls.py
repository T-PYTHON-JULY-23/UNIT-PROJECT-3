from django.urls import path,include
from . import views

app_name = 'service'

urlpatterns = [
    path('add_service/',views.add_dessert_view,name='add_dessert_view'),
    path('all_service/',views.all_dessert_view,name='all_dessert_view'),
    path('detail/<dessert_id>',views.dessert_detail_view,name='dessert_detail_view'),
    path('update/<dessert_id>',views.update_dessert_view,name='update_dessert_view'),
    path('delete/<dessert_id>',views.delete_dessert_view,name='delete_dessert_view'),  
    path("order/<dessert_id>/", views.add_order_view, name="add_order_view"),

]