from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

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


@login_required
def desk_view(request):
    """Create desk controller."""
    tasks = Task.objects.filter(author=request.user)
    return render(request, "board.html", {"tasks": tasks})
