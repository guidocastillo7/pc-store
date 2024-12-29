from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart, name="cart"),
    path("add_product/<int:product_id>", views.add_product, name="add_product"),
    path("remove_product/<int:product_id>", views.remove_product, name="remove_product"),
    path("clear_cart/", views.clear_cart, name="clear_cart")
]
