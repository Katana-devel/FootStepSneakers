from pathlib import Path
from uuid import uuid4

from django.conf import settings
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._discount = 0  # encapsulated in-memory attribute, not stored in DB

    # --- Properties ---

    @property
    def full_name(self):
        return f"{self.brand} {self.model}"

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self._discount = value

    @property
    def discounted_price(self):
        return int(self.price * (1 - self._discount / 100))

    # --- Class methods ---

    @classmethod
    def get_public(cls):
        return cls.objects.filter(is_public=True)

    def __str__(self):
        return self.full_name


class Picture(models.Model):

    # --- Static methods (utilities that don't need instance or class) ---

    @staticmethod
    def validate_file_size(value):
        if value.size > 1_000_000:
            raise ValidationError('Maximum file size is 1MB')
        return value

    @staticmethod
    def generate_upload_path(instance, filename):
        upload_to = Path(instance.user.username) if instance.user else Path('images')
        ext = Path(filename).suffix
        return str(upload_to / f"{uuid4().hex}{ext}")

    # --- Class methods ---

    @classmethod
    def get_for_user(cls, user):
        return cls.objects.filter(user=user)

    # --- Fields ---

    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name="pictures")
    # .__func__ unwraps the staticmethod descriptor so Django can use it as a callable
    path = models.ImageField(
        upload_to=generate_upload_path.__func__,
        validators=[validate_file_size.__func__],
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )


