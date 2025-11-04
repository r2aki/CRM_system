from django.urls import path
from .views import (
    LeadListView, LeadDetailView, LeadCreateView,
    LeadUpdateView, LeadDeleteView, LeadConvertView
)

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('list/', LeadListView.as_view(), name='lead_list_alt'),
    path('all/', LeadListView.as_view(), name='lead_list_all'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('detail/<int:pk>/', LeadDetailView.as_view(), name='lead_detail_alt'),
    path('new/', LeadCreateView.as_view(), name='lead_create'),
    path('create/', LeadCreateView.as_view(), name='lead_create_alt'),
    path('add/', LeadCreateView.as_view(), name='lead_create_add'),
    path('<int:pk>/edit/', LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead_update_alt'),
    path('<int:pk>/change/', LeadUpdateView.as_view(), name='lead_update_change'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),
    path('<int:pk>/remove/', LeadDeleteView.as_view(), name='lead_delete_alt'),
    path('<int:pk>/convert/', LeadConvertView.as_view(), name='lead_convert'),
    path('<int:pk>/to-customer/', LeadConvertView.as_view(), name='lead_convert_alt'),
]