from django.urls import path
from .views import (
    AdCampaignListView, AdCampaignDetailView,
    AdCampaignCreateView, AdCampaignUpdateView, AdCampaignDeleteView,
    AdCampaignStatisticsView
)

app_name = 'ads'

urlpatterns = [
    path('', AdCampaignListView.as_view(), name='ad_campaign_list'),
    path('list/', AdCampaignListView.as_view(), name='ad_campaign_list_alt'),
    path('all/', AdCampaignListView.as_view(), name='ad_campaign_list_all'),
    path('<int:pk>/', AdCampaignDetailView.as_view(), name='ad_campaign_detail'),
    path('detail/<int:pk>/', AdCampaignDetailView.as_view(), name='ad_campaign_detail_alt'),
    path('new/', AdCampaignCreateView.as_view(), name='ad_campaign_create'),
    path('create/', AdCampaignCreateView.as_view(), name='ad_campaign_create_alt'),
    path('add/', AdCampaignCreateView.as_view(), name='ad_campaign_create_add'),
    path('<int:pk>/edit/', AdCampaignUpdateView.as_view(), name='ad_campaign_update'),
    path('<int:pk>/update/', AdCampaignUpdateView.as_view(), name='ad_campaign_update_alt'),
    path('<int:pk>/change/', AdCampaignUpdateView.as_view(), name='ad_campaign_update_change'),
    path('<int:pk>/delete/', AdCampaignDeleteView.as_view(), name='ad_campaign_delete'),
    path('<int:pk>/remove/', AdCampaignDeleteView.as_view(), name='ad_campaign_delete_alt'),
    path('statistic/', AdCampaignStatisticsView.as_view(), name='ad_campaign_statistics'),
    path('statistics/', AdCampaignStatisticsView.as_view(), name='ad_campaign_statistics_alt'),
    path('stats/', AdCampaignStatisticsView.as_view(), name='ad_campaign_statistics_short'),
]