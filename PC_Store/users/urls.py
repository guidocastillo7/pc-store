from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("register/", views.register, name="register"),
    path("create_user/", views.create_user, name="create_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("user_profile/", views.user_profile, name="user_profile"),
    path("edit_user_data/", views.edit_user_data, name="edit_user_data")
]
