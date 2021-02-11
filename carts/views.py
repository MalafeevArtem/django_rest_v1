from rest_framework import generics , mixins , viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from carts.models import Cart, CartItem
from carts.paginations import CartItemPagination
from carts.serializers import CartItemSerializer, CartSerializer


class CartViewSet(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.cart


class CarItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    pagination_class = CartItemPagination

    def get_object(self):
        return get_object_or_404(self.request.user.cart_items, pk=self.kwargs['pk'])

    def get_queryset(self):
        queryset = self.request.user.cart
        return queryset.cart_items.all()
