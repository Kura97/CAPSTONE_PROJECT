from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    #for Product
    path("list_products/", views.list_products, name="list products"),
    path("add_product/", views.add_product, name="Add product"),
    path("update_product/<product_id>", views.update_product, name="update product"),
    path("delete_product/<product_id>", views.delete_product, name="delete product"),

 
]