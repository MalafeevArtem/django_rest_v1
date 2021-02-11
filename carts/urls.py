from django.urls import path

from rest_framework.routers import DefaultRouter

from carts.views import CarItemViewSet, CartViewSet


cart_router = DefaultRouter()
cart_router.register('items', CarItemViewSet, basename='cart_item')

urlpatterns = [
    path(r'', CartViewSet.as_view(), name='cart')
]

urlpatterns += cart_router.urls
