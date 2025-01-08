from django.shortcuts import (render, redirect)
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


@login_required(login_url="/users/login")
def checkout(request):
    if not request.session.get("cart"):
        return redirect("/cart")

    address = request.user.address
    cart = Cart(request)

    context = {
        "address": address,
        "total_amount": cart.get_total_amount()
    }

    return render(request, "checkout.html", context)
