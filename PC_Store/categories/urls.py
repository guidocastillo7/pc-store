from django.urls import path
from . import views

urlpatterns = [
    path("monitors/", views.monitors, name="monitors"),
    path("ssd/", views.ssd, name="ssd"),
    path("processors/", views.processors, name="processors"),
    path("graphic_cards/", views.graphic_cards, name="graphic_cards"),
]
