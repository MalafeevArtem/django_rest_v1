from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.filters import OrderingFilter

from items.filters import ItemFilter
from items.models import Item
from items.paginations import ItemPagination
from items.serializers import ItemSerializer


class ItemViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    pagination_class = ItemPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ItemFilter
