from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"

        self.fields["username"].help_text = ""
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username[0].isdigit():
            raise ValidationError(
                "Username must start with a letter"
            )

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if email[0].isdigit():
            raise ValidationError(
                "Email must start with a letter"
            )

        return email

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        username = self.cleaned_data.get("username")

        if len(password) < 8:
            raise ValidationError(
                "Password must be at least 8 characters"
            )

        if len(password) > 16:
            raise ValidationError(
                "Password must not exceed 16 characters"
            )

        if password.isdigit():
            raise ValidationError(
                "Password cannot contain only numbers"
            )

        if username and password.lower() == username.lower():
            raise ValidationError(
                "Password cannot be same as username"
            )

        return password