from pathlib import Path
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

class Sneakers(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    posted_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)


    def __str__(self):
        return self.model


def validate_file_size(value):
    filesize = value.size

    if filesize > 1_000_000:
        raise ValidationError('Максимальний розмір файлу 1Мб')
    return value


def upload_image(instance, filename):
    upload_to = Path(instance.user.username) if instance.user else Path('images')
    ext = Path(filename).suffix
    new_filename = f"{uuid4().hex}{ext}"
    return str(upload_to / new_filename)


class Picture(models.Model):
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name="pictures")
    path = models.ImageField(upload_to=upload_image, validators=[validate_file_size])
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)


