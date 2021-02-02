from datetime import datetime

import requests
from django.core.management import BaseCommand

from reviews.models import Review
from users.models import User

URL = 'https://jsonkeeper.com/b/1LJM'


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(url=URL).json()

        for review in response:
            rev = Review.objects.update_or_create(
                id=review['id'],
                defaults={
                    'author': User.objects.get(id=review['author']),
                    'text': review['content'],
                    'status': review['status'],
                }
            )

            if review['created_at ']:
                rev[0].created_at = datetime.strptime(review['created_at '], '%Y-%m-%d').date()
                rev[0].save()
            if review['published_at']:
                rev[0].published_at = datetime.strptime(review['published_at'], '%Y-%m-%d').date()
                rev[0].save()
