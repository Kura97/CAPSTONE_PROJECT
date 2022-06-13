from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("list_products/", views.list_products, name="list products"),
    path("add_product/", views.add_product, name="Add product"),
    
]