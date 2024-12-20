from django.shortcuts import render


def orders(request):
    return render(request, "orders.html")


def order_details(request):
    return render(request, "order_details.html")
