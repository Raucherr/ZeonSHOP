from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response



class ListCollectionsPagination(PageNumberPagination):
    """Установить определенную нумерацию страниц для списка коллекций"""

    page_size = 8


class CollectionsListView(generics.ListAPIView):
    """Просмотреть, чтобы просмотреть все коллекции."""

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


class ProductLikeView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFavoriteSerializer
    lookup_field = 'pk'


class ProductsFavoritesView(generics.ListAPIView):
    """список избранных."""
    queryset = Product.objects.filter(favorite=True)
    serializer_class = ProductsSerializer
    pagination_class = ProductsInCollectionPagination12


class ProductsCartView(generics.ListAPIView):
    """список всех продуктов в корзины."""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class ProductCartView(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр для обновления, Удаления товара в корзине."""
    queryset = Cart.objects.all()
    serializer_class = CartUpdateSerializer


class CartCreateView(generics.CreateAPIView):
    """вьюшка добавления товара в корзину"""
    serializer_class = CartCreateSerializer
    permission_classes = [permissions.AllowAny]


@api_view()
def order_info_view(request):
    """Возвращает всю инфу про заказ"""

    return Response({
        "Количество линеек": calculate_order_info()[0],
        "Количество товаров": calculate_order_info()[1],
        "Стоимость": calculate_order_info()[2],
        "Скидка": calculate_order_info()[4],
        "Итого к оплате": calculate_order_info()[3]
        })


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()


class OrdersHistoryView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrdersHistorySerializer