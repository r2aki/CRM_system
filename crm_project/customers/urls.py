from django.urls import path
from .views import (
    CustomerListView, CustomerDetailView,
    CustomerCreateView, CustomerUpdateView, CustomerDeleteView
)

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('list/', CustomerListView.as_view(), name='customer_list_alt'),
    path('all/', CustomerListView.as_view(), name='customer_list_all'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('detail/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail_alt'),
    path('new/', CustomerCreateView.as_view(), name='customer_create'),
    path('create/', CustomerCreateView.as_view(), name='customer_create_alt'),
    path('add/', CustomerCreateView.as_view(), name='customer_create_add'),
    path('<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_update'),
    path('<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update_alt'),
    path('<int:pk>/change/', CustomerUpdateView.as_view(), name='customer_update_change'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('<int:pk>/remove/', CustomerDeleteView.as_view(), name='customer_delete_alt'),
]