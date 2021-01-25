import os
import urllib

import requests


from django.core.management import BaseCommand

from items.models import Item
from stepik_rest.settings import BASE_DIR, MEDIA_ROOT

URL = 'https://jsonkeeper.com/b/L6UH'


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(url=URL).json()

        for item in response:
            image_url = item['image']
            image_name = item['image'].split('/')[-1]
            path = os.path.join(BASE_DIR, MEDIA_ROOT, 'items')
            os.makedirs(path, exist_ok=True)
            urllib.request.urlretrieve(image_url, os.path.join(path, image_name))

            Item.objects.update_or_create(
                id=item['id'],
                defaults={
                    'title': item['title'],
                    'description': item['description'],
                    'image': os.path.join('items', image_name),
                    'weight': item['weight_grams'],
                    'price': item['price']
                }
            )
