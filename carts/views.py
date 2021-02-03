from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet

from carts.models import Cart, CartItem
from carts.paginations import CartItemPagination
from carts.serializers import CartItemSerializer, CartSerializer


class CartViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class CarItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    pagination_class = CartItemPagination
