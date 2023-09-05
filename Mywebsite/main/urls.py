from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.profile_view, name="profile_view"),
    path('main/education.html',views.education_view,name="education_view"),
    path('main/about.html',views.about_view,name="about_view"),
    path('main/home.html', views.home_view, name="home_view"),
    path("main/add_shirt.html/", views.add_shirt_view, name="add_shirt_view"),
    path("main/add_childrenShirt.html/", views.add_childrenShirt_view, name="add_childrenShirt_view"),
    path("main/shirts.html/", views.shirts_view, name="shirts_view"),
    path("main/shirt_detail.html/<shirt_id>/", views.shirt_detail_view, name="shirt_detail_view"),
    path("main/child_shirt_detail.html/<child_shirt_id>/", views.child_shirt_detail_view, name="child_shirt_detail_view"),
    path("main/update_child_shirt/<child_shirt_id>/", views.child_shirt_update_view, name="child_shirt_update_view"),
    path("main/update_shirt/<shirt_id>/", views.shirt_update_view, name="shirt_update_view"),
    path("delete/<shirt_id>/", views.shirt_delete_view, name="shirt_delete_view"),
    path("delete/<child_shirt_id>/", views.child_shirt_delete_view, name="child_shirt_delete_view"),
    path("search/", views.shirts_search_view, name="shirts_search_view"),
    path("product/add/shirt/<shirt_id>/", views.add_product_view, name="add_product_view"),
    path("product/add/child/<child_shirt_id>/", views.add_child_shirt_product_view, name="add_child_shirt_product_view"),
    path("product/remove/<child_shirt_id>/", views.remove_child_shirt_product_view, name="remove_child_shirt_product_view"),
    path("product/remove/<product_id>/", views.remove_product_view, name="remove_product_view"),
    path("product/", views.user_product_view, name="user_product_view"),
    path("main/checkout.html/", views.checkout_view, name="checkout_view"),


]
