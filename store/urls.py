from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("/", views.all_products, name="all_products"),
    path("<slug:slug>", views.product_details, name="product_details"),
    path("<slug:slug>/", views.category_details, name="category_details"),
]
