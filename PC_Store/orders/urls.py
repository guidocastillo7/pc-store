from django.urls import path
from . import views

urlpatterns = [
    path("", views.orders, name="orders"),
    path("order_details/", views.order_details, name="order_details"),
]
