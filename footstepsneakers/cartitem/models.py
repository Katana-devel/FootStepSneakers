from django.conf import settings
from django.db import models

from product.models import Sneakers


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    # --- Properties ---

    @property
    def total_price(self):
        return self.sneakers.price * self.quantity

    # --- Class methods ---

    @classmethod
    def get_for_user(cls, user):
        return cls.objects.filter(user=user)

    def __str__(self):
        return f"{self.sneakers.full_name} x{self.quantity}"