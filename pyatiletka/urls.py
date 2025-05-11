"""
URL configuration for pyatiletka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib.auth.views import LoginView
from django.urls import path

from main import views as main_views

urlpatterns = [
    path("", main_views.desk_view),
    path("/login", LoginView.as_view(template_name="login.html")),
    path("/logout", LoginView.as_view()),
    path("/register", main_views.registration_view),
    path("/tasks/<int:task_id>/move", main_views.move_task_view),
    path("/tasks/<int:task_id>", main_views.view_task_view),
    path("/tasks/<int:task_id>/delete", main_views.delete_task),
    path("/new-task", main_views.create_task_view),
    path("/tasks/<int:task_id>/edit", main_views.edit_task_view),
]
