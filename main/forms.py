
from django import forms

from main.models import Task


class RegistrationForm(forms.Form):
    """Form for registering a new user."""

    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())


class MoveTaskForm(forms.Form):
    """Form for moving a task."""

    state_to = forms.ChoiceField(choices=Task.Status)


class CreateTaskControllerForm(forms.Form):
    """класс отслеживания задач."""

    title = forms.CharField(max_length=110)
    text = forms.CharField(widget=forms.Textarea())
    deadline = forms.DateTimeField(required=False, widget=forms.DateTimeInput())
