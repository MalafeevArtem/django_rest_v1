from django.db import models

from users.models import User


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='reviews')
    text = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=32)

    def __str__(self):
        return '{0}'.format(self.author)
