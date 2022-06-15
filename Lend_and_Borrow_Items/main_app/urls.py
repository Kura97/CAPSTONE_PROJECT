from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    #for Product model
    path("list_products/", views.list_products, name="list products"),
    path("add_product/", views.add_product, name="Add product"),
    path("update_product/<product_id>", views.update_product, name="update product"),
    path("delete_product/<product_id>", views.delete_product, name="delete product"),
    path("search_product/<product_title>", views.search_product, name="search product"),

    #for Review model
    path("list_reviews/", views.list_reviews, name="list reviews"),
    path("add_review/", views.add_review, name="Add review"),
    path("update_review/<review_id>", views.update_review, name="update review"),
    path("delete_review/<review_id>", views.delete_review, name="delete review"),

    #for Profile model
    path("list_profiles/", views.list_profiles, name="list profiles"),
    path("add_profile/", views.add_profile, name="Add profile"),
    path("update_profile/<profile_id>", views.update_profile, name="update profile"), 
]