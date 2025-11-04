from django.urls import path
from .views import (
    ProductListView, ProductDetailView,
    ProductCreateView, ProductUpdateView, ProductDeleteView
)

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('list/', ProductListView.as_view(), name='product_list_alt'),
    path('all/', ProductListView.as_view(), name='product_list_all'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail_alt'),
    path('new/', ProductCreateView.as_view(), name='product_create'),
    path('create/', ProductCreateView.as_view(), name='product_create_alt'),
    path('add/', ProductCreateView.as_view(), name='product_create_add'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update_alt'),
    path('<int:pk>/change/', ProductUpdateView.as_view(), name='product_update_change'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/remove/', ProductDeleteView.as_view(), name='product_delete_alt'),
]