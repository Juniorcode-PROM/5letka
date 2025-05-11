from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import RegistrationForm
from main.models import Task


def registration_view(request):
    """Registration controller."""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            User.objects.create_user(username=username, password=password)
            return redirect("/")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


def delete_task(request, task_id):
    """Пощадите _/\_"""
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("/")
