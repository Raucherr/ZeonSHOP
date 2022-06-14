from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Collection, Product
from .serializers import CollectionsSerializer, ProductsSerializer,\
    ProductsInCollectionSerializer


class ListCollectionsPagination(PageNumberPagination):
    """Установить определенную нумерацию страниц для списка коллекций"""

    page_size = 8


class CollectionsListView(generics.ListAPIView):
    """VПросмотреть, чтобы просмотреть все коллекции."""

    queryset = Collection.objects.all()
    serializer_class = CollectionsSerializer
    pagination_class = ListCollectionsPagination


class ProductsInCollectionPagination12(PageNumberPagination):
    """Установить определенную нумерацию страниц для списка товаров в определенной коллекции.."""

    page_size = 12


class CollectionDetailView(generics.ListAPIView):
    """Получить список продуктов по выбранной коллекции."""
    queryset = Product.objects.all()
    serializer_class = ProductsInCollectionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection']
    pagination_class = ProductsInCollectionPagination12




class ProductsNoveltiesPagination(PageNumberPagination):
    """Установите определенную нумерацию страниц для списка продуктов в определенной коллекции"""

    page_size = 5


class ProductNoveltiesView(generics.ListAPIView):
    """Перечислите все «Новинки» продуктов."""
    queryset = Product.objects.filter(novelty=True)
    serializer_class = ProductsSerializer
    pagination_class = ProductsNoveltiesPagination


class ProductsInCollectionPagination5(PageNumberPagination):
    """Установите конкретную разбивку на страницы для списка продуктов в определенной коллекции."""

    page_size = 5


class ProductsListView(generics.ListAPIView):
    """Получить список продуктов по выбранной коллекции."""
    queryset = Product.objects.all()
    serializer_class = ProductsInCollectionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection']
    pagination_class = ProductsInCollectionPagination5


class ProductDetailView(generics.RetrieveAPIView):
    """Детальный вид объекта Product по id/pk."""
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer