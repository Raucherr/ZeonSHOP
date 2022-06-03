
from django.urls import path
from .views import CollectionsListView, CollectionDetailView

urlpatterns = [
    path('collections/', CollectionsListView.as_view(), name='collections'),
    path('collections/detail/', CollectionDetailView.as_view()),
]