from django import forms


class RegistrationForm(forms.Form):
    """Form for registering a new user."""

    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
