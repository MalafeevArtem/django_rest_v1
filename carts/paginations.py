from rest_framework.pagination import LimitOffsetPagination


class CartItemPagination(LimitOffsetPagination):
    default_limit = 5
