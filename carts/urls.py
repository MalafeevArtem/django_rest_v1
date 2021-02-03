from rest_framework.routers import DefaultRouter

from carts.views import CarItemViewSet, CartViewSet


item_router = DefaultRouter()
item_router.register('items', CarItemViewSet, basename='item')
item_router.register('', CartViewSet, basename='item')

urlpatterns = item_router.urls
