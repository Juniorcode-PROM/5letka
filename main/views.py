from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import CreateTaskControllerForm, MoveTaskForm, RegistrationForm
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
    if request.method == "POST":
        form = CreateTaskControllerForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data["title"]
            task.text = form.cleaned_data["text"]
            task.deadline = form.cleaned_data["deadline"]
            task.save()
            return redirect("/")
    else:
        form = CreateTaskControllerForm({
            "title": task.title,
            "text": task.text,
            "deadline": task.deadline,
        })
    return render(request, "edit-task.html", {"form": form})

@login_required
def move_task_view(request, task_id):
    """Move a task to another column."""
    task = get_object_or_404(Task, id=task_id)
    if task.author != request.user:
        raise PermissionDenied
    form = MoveTaskForm(request.GET)
    if form.is_valid():
        task.status = form.cleaned_data["state_to"]
        task.save()
    return redirect("/")


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
            return redirect("/")
    else:
        form = CreateTaskControllerForm()
    return render(request, "tasks_maker.html", {"form": form})


@login_required
def desk_view(request):
    """Create desk controller."""
    tasks = Task.objects.filter(author=request.user)
    return render(request, "board.html", {"tasks": tasks})
