from django.urls import path
from .views import (
    ContractListView, ContractDetailView,
    ContractCreateView, ContractUpdateView, ContractDeleteView
)

app_name = 'contracts'

urlpatterns = [
    path('', ContractListView.as_view(), name='contract_list'),
    path('list/', ContractListView.as_view(), name='contract_list_alt'),
    path('all/', ContractListView.as_view(), name='contract_list_all'),
    path('<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),
    path('detail/<int:pk>/', ContractDetailView.as_view(), name='contract_detail_alt'),
    path('new/', ContractCreateView.as_view(), name='contract_create'),
    path('create/', ContractCreateView.as_view(), name='contract_create_alt'),
    path('add/', ContractCreateView.as_view(), name='contract_create_add'),
    path('<int:pk>/edit/', ContractUpdateView.as_view(), name='contract_update'),
    path('<int:pk>/update/', ContractUpdateView.as_view(), name='contract_update_alt'),
    path('<int:pk>/change/', ContractUpdateView.as_view(), name='contract_update_change'),
    path('<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete'),
    path('<int:pk>/remove/', ContractDeleteView.as_view(), name='contract_delete_alt'),
]