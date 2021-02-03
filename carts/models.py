from django.conf import settings
from django.db import models

from items.models import Item


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='users')
    items = models.ManyToManyField(Item, through='CartItem', blank=True)

    @property
    def total_cost(self):
        return sum(self.carts.total_price)


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name='carts')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,
                             related_name='carts')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    @property
    def total_price(self):
        return self.quantity * self.price
