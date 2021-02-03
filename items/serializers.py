from rest_framework import serializers

from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'image', 'weight', 'price']

        extra_kwargs = {
            'weight': {'min_value': -2147483647, 'max_value': 2147483647}
        }
