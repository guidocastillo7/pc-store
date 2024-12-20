from django.shortcuts import render


def monitors(request):
    return render(request, "monitors.html")


def ssd(request):
    return render(request, "ssd.html")


def processors(request):
    return render(request, "processors.html")


def graphic_cards(request):
    return render(request, "graphic_cards.html")
