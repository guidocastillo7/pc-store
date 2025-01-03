from django.shortcuts import (render, redirect)
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import (UserRegisterForm, UserLoginForm)


def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect("/")

        else:
            form_error = [error for error in form.errors.values()]
            login_form = UserLoginForm()

            context = {"login_form": login_form,
                       "form_error": form_error[0]}

            return render(request, "login.html", context)

    else:
        login_form = UserLoginForm()
        context = {"login_form": login_form}

        return render(request, "login.html", context)


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


def create_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user_data = form.cleaned_data

            try:
                new_user = form.save(commit=False)
                new_user.first_name = user_data["first_name"].capitalize()
                new_user.last_name = user_data["last_name"].capitalize()
                new_user.save()

                login(request, new_user)

                return redirect("/")

            except Exception as e:
                messages.error(request, "Error creating user, please try again")
                register_form = UserRegisterForm(request.POST)
                print(f"error {e}")
                context = {"register_form": register_form}

                return render(request, "register.html", context)

        else:
            form_errors = form.errors
            register_form = UserRegisterForm(request.POST)

            context = {"register_form": register_form,
                       "form_errors": form_errors}

            return render(request, "register.html", context)

    return redirect("/users/register")


def logout_user(request):
    logout(request)

    return redirect("/")
