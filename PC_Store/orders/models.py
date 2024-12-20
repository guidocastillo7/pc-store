from django.db import models
from users.models import User
from products.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed")
    ]

    order_number = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default="pending",
                              choices=STATUS_CHOICES)

    def __str__(self):
        return self.order_number


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField(default=1)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.product.name
