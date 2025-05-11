from django import forms


class RegistrationForm(forms.Form):
    """Form for registering a new user."""

    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())


class CreateTaskControllerForm(forms.Form):
    """класс отслеживания задач"""

    title = forms.CharField(max_length=110)
    text = forms.CharField(widget=forms.Textarea())
    deadline = forms.DateTimeField(null=True, default=None)
