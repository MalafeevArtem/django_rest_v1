from rest_framework import serializers

from carts.models import Cart, CartItem
from items.models import Item


class CartItemSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())

    class Meta:
        model = CartItem
        fields = ['id', 'item', 'cart', 'item_id',
                  'quantity', 'price', 'total_price']

        extra_kwargs = {
            'quantity': {'min_value': 0, 'max_value': 2147483647}
        }


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_cost']
