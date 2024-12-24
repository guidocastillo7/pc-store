from django.shortcuts import render
from .models import Product


def products(request, product_id):
    product = Product.objects.get(pk=product_id)

    context = {
        "product": product
    }

    return render(request, "products.html", context)
