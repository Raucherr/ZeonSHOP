from django.contrib import admin
from django.contrib import admin
from .models import *


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    """Representation of a model 'Collection' in the admin interface."""
    list_display = ('title',)
