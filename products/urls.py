from django.urls import path
from .views import *

urlpatterns = [
    path('collections/', CollectionsListView.as_view(), name='collections'),
    path('collections/detail/', CollectionDetailView.as_view()),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('products/<int:pk>/favorite/', ProductLikeView.as_view()),
    path('products/favorites/', ProductsFavoritesView.as_view(),
         name='products_favorites'),
    path('cart/', ProductsCartView.as_view(), name='cart_list'),
    path('cart/<int:pk>/', ProductCartView.as_view(), name='cart_detail'),
    path('products/add_to_cart/', CartCreateView.as_view()),
    path('order/total_sum/', order_info_view),
    path('order/create/', OrderCreateView.as_view()),
    path('order/history/', OrdersHistoryView.as_view()),
]