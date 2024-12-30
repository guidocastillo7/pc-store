from typing import Any
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={"class":"form-control"})
    )
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={"class":"form-control"})
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={"class":"form-control"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class":"form-control"})
        self.fields["password1"].widget.attrs.update({"class":"form-control"})
        self.fields["password2"].widget.attrs.update({"class":"form-control"})
