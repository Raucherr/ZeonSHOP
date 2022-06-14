from django.contrib import admin
from .models import Collection, ProductStyles, Product


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    """Представление модели "Коллекция" в интерфейсе администратора."""
    list_display = ('title',)


class ProductObjectsAdmin(admin.StackedInline):
    """Разрешить администратору добавлять изображения и цвета для продукта (максимум 8)."""
    model = ProductStyles
    max_num = 8


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Представление модели «Товар» в интерфейсе администратора."""
    inlines = [ProductObjectsAdmin]
    list_display = ('title', 'article', 'size_line', 'quantity_in_line',
                    'collection')


