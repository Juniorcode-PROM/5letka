from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Task(models.Model):
    """Это крутая молодёжная моделька задачи."""

    class Status(models.TextChoices):
        """Это крутая молодёжная моделька задачи номер 2!."""

        NOT_STARTED = "N", "Not started"
        IN_PROGRESS = "I", "In progress"
        DONE = "D", "Done"

    title = models.CharField(max_length=110)
    text = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1, choices=Status, default=Status.NOT_STARTED
    )
    deadline = models.DateTimeField(null=True, default=None)

    @property
    def short_text(self):
        return self.text[:min(len(self.text), 32)]
