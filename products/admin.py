from django.contrib import admin
from django.contrib import admin
from .models import *


class ProductStylesAdmin(admin.StackedInline):
    """Allow to admin add images and colors for product (maximum 8)."""
    model = ProductStyles
    max_num = 8

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Representation of a model 'Product' in the admin interface."""
    inlines = [ProductStylesAdmin]
    list_display = ('title', 'article', 'size_line', 'quantity_in_line',
                    'collection')

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    """Representation of a model 'Collection' in the admin interface."""
    list_display = ('title',)

