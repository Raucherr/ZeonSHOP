from rest_framework import serializers
from .models import *


class CollectionsSerializer(serializers.ModelSerializer):
    """перевод в JSON."""

    class Meta:
        model = Collection
        fields = '__all__'


class ProductStylesSerializer(serializers.ModelSerializer):
    """Перевод данных о вариантах продукта в формат JSON."""

    class Meta:
        model = ProductStyles
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    """варианты продукта в JSON."""
    product_styles = ProductStylesSerializer(many=True)
    collection = CollectionsSerializer()

    class Meta:
        model = Product
        exclude = ['bestseller', 'novelty']


class ProductsInCollectionSerializer(serializers.ModelSerializer):
    """Сериализация продуктов в определенной коллекции"""
    product_objects = ProductStylesSerializer(many=True)
    collection = CollectionsSerializer()

    class Meta:
        model = Product
        fields = ['collection', 'id', 'product_objects', 'title',
                  'actual_price', 'old_price', 'discount',
                  'size_line', 'favorite']


class ProductFavoriteSerializer(serializers.ModelSerializer):
    """Сериализация для проверки like/Unlike"""

    class Meta:
        model = Product
        fields = ['id', 'title', 'favorite']
        read_only_fields = ('id', 'collection', 'title', 'article',
                            'actual_price', 'old_price', 'discount',
                            'description', 'size_line', 'tissue_composition',
                            'quantity_in_line', 'material', 'bestseller',
                            'novelty')


class ProductsForCart(serializers.ModelSerializer):
    """Сериализация продуктов в определенной коллекции"""

    class Meta:
        model = Product
        fields = ['id', 'title', 'size_line',
                  'actual_price', 'old_price', 'quantity_in_line']


class ProductsInCartSerializer(serializers.ModelSerializer):
    """Сериализация товаров в корзине"""
    product = ProductsForCart()

    class Meta:
        model = ProductStyles
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    """Сериализация товаров в корзине"""
    product = ProductsInCartSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity']


class CartUpdateSerializer(serializers.ModelSerializer):
    """Сериализация товара в корзине для увеличения/уменьшения количества товара."""
    product = ProductsInCartSerializer(read_only=True)
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = Cart
        fields = ['product', 'quantity']
        read_only_fields = ('id', 'product')


class CartCreateSerializer(serializers.ModelSerializer):
    """Для создания нового объекта корзины."""
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = Cart
        fields = ['product', 'quantity']