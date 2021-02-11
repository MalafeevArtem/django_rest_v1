from django.contrib.auth.models import AbstractUser
from django.db import models

from carts.models import Cart


class User(AbstractUser):
    middle_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=128)

    def __str__(self):
        return '{0} {1}'.format(self.username, self.last_name)

    @property
    def cart(self):
        cart, _ = Cart.objects.get_or_create(user=self)
        return cart
