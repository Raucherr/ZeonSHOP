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