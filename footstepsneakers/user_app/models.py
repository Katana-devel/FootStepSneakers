from django.contrib.auth.models import AbstractUser
from django.db import models


class SneakerUser(AbstractUser):
    bio = models.TextField(blank=True, default='')

    def __str__(self):
        return f"{self.username} ({self.email})"

    @property
    def display_name(self):
        full = f"{self.first_name} {self.last_name}".strip()
        return full if full else self.username
