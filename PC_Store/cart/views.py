from django.shortcuts import render, redirect
from cart.cart import Cart
from products.models import Product


def cart(request):
    cart = Cart(request)

    context = {
        "cart": cart.cart,
        "total_amount": cart.get_total_amount()
    }

    return render(request, "cart.html", context)


def add_product(request, product_id):
    if request.method == "POST":
        cart = Cart(request)
        product = Product.objects.get(pk=product_id)
        quantity = int(request.POST.get("quantity"))
        cart.add_product(product, quantity)

        return redirect(f"/products/{product_id}")


def remove_product(request, product_id):
    if request.method == "POST":
        cart = Cart(request)
        cart.remove_product(product_id)

        return redirect("/cart")


def clear_cart(request):
    cart = Cart(request)
    cart.clear()

    return render(request, "cart.html")
