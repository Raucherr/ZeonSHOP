from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend



class ListCollectionsPagination(PageNumberPagination):
    """
    нумерация страниц для коллекци
    """
    page_size = 8

class CollectionsListView(generics.ListAPIView):
    """все коллекции."""
    queryset = Collection.objects.all()
    serializer_class = CollectionsSerializer
    pagination_class = ListCollectionsPagination

class ProductsInCollectionPagination12(PageNumberPagination):
    """страницы в коллекции."""
    page_size = 12




class ProductsListView(generics.ListAPIView):
    """список продуктов определенной коллекции."""
    queryset = Product.objects.all()
    serializer_class = ProductsInCollectionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection']
    pagination_class = ProductsInCollectionPagination12


class ProductDetailView(generics.RetrieveAPIView):
    """Просмотр деталей продукта по id/pk."""
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


