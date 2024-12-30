from django.shortcuts import render
from .forms import UserRegisterForm


def login(request):
    return render(request, "login.html")


def register(request):
    register_form = UserRegisterForm()
    register_form.order_fields([
        "username",
        "email",
        "first_name",
        "last_name",
        "password1",
        "password2"
    ])

    context = {
        "register_form": register_form
    }

    return render(request, "register.html", context)
