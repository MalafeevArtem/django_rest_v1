from django.conf import settings
from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to=settings.MEDIA_ITEM_DIR)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.title
