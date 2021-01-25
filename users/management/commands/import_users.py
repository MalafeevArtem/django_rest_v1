import requests
from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from users.models import User

URL = 'https://jsonkeeper.com/b/96RI'


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(url=URL).json()

        for user in response:
            User.objects.update_or_create(
                id=user['id'],
                defaults={
                    'email': user['email'],
                    'username': user['email'].split('@')[0],
                    'password': make_password(user['password']),
                    'last_name': user['info']['surname'],
                    'first_name': user['info']['name'],
                    'middle_name': user['info']['patronymic'],
                    'phone_number': user['contacts']['phoneNumber'],
                    'address': user['city_kladr'],
                    'is_superuser': user['premium'],
                }
            )
