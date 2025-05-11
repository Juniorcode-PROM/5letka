from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import CreateTaskControllerForm, RegistrationForm
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


def view_task_view(request, task_id):
    """ъэ функция в 2 долбанных строчки, делающая очень много."""
    task = get_object_or_404(Task, id=task_id)
    # TODO: fill template name
    return render(request, ".html", {"task": task})


def delete_task(request, task_id):
    r"""Пощадите _/\_."""
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("/")


@login_required
def create_task_view(request):
    """CreateTaskController."""
    if request.method == "POST":
        form = CreateTaskControllerForm(request.POST)
        if form.is_valid():
            title= form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            deadline = form.cleaned_data["deadline"]
            Task.objects.create(
                title=title, text=text,
                deadline=deadline, author=request.user
            )
    else:
        form = CreateTaskControllerForm()
    return render(request, "tasks_maker.html", {"form": form})
