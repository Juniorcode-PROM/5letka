from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import MoveTaskForm, RegistrationForm
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


@login_required
def move_task_view(request, task_id):
    """Move a task to another column."""
    task = get_object_or_404(Task, id=task_id)
    if task.author != request.user:
        raise PermissionDenied
    form = MoveTaskForm(request.POST)
    if form.is_valid():
        task.status = form.cleaned_data["state_to"]
        task.save()
    return redirect("/")
