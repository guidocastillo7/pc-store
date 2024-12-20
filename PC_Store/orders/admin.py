from django.contrib import admin
from .models import Order, OrderDetail


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "order_number",
        "status",
        "created_at"
    )


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "product",
        "quantity",
        "amount"
    )
