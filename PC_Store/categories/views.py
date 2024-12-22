from django.shortcuts import render
from products.models import Product


def monitors(request):
    monitors = Product.objects.filter(
        category__name="Monitors"
    )

    context = {
        "monitors": monitors
    }

    return render(request, "monitors.html", context)


def ssd(request):
    ss_drives = Product.objects.filter(
        category__name="SSD"
    )

    context = {
        "ss_drives": ss_drives
    }

    return render(request, "ssd.html", context)


def processors(request):
    processors = Product.objects.filter(
        category__name="Processors"
    )

    context = {
        "processors": processors
    }

    return render(request, "processors.html", context)


def graphic_cards(request):
    graphic_cards = Product.objects.filter(
        category__name="Graphic Cards"
    )

    context = {
        "graphic_cards": graphic_cards
    }

    return render(request, "graphic_cards.html", context)
