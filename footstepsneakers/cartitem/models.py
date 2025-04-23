from django.db import models

from django.contrib.auth.models import User

from product.models import Sneakers


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)