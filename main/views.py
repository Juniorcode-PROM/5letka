from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render, get_object_or_404

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


def edit_task_view(request, task_id):
    """функция для изменения задачи пользователем."""
    task = get_object_or_404(Task, id=task_id)
    if task.author != request.user:
        raise PermissionDenied
    if request.metho