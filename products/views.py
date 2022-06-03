from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class ListCollectionsPagination(PageNumberPagination):
    """
    нумерация страниц для коллекций
    """

    page_size = 8

class CollectionsListView(generics.ListAPIView):
    """View to list all Collections."""

    queryset = Collection.objects.all()
    serializer_class = CollectionsSerializer
    pagination_class = ListCollectionsPagination

class ProductsInCollectionPagination12(PageNumberPagination):
    """Set specific pagination for Product list in definite Collection."""

    page_size = 12