from typing import Any
from django import forms
from .models import User
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm)


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

    class Meta:
        model = User
        fields = ["username", "email", "first_name",
                  "last_name", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        self.fields["username"].widget.attrs.update({"class":"form-control"})
        self.fields["password"].widget.attrs.update({"class":"form-control"})


class EditUserDataForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name",
                  "last_name", "address", "phone"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "style": "resize: none;"
            })
        }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        filtered_users = User.objects.filter(
            username__iexact=username
        ).exclude(pk=self.instance.id)

        if username and filtered_users.exists():
            raise forms.ValidationError("A user with that username already exists.")

        else:
            return username
