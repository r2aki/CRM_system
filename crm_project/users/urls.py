from django.urls import path
from .views import (
    DashboardView, UserListView, UserDetailView, UserCreateView,
    UserUpdateView, UserDeleteView, UserProfileUpdateView
)

app_name = 'users'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('dashboard/', DashboardView.as_view(), name='dashboard_alt'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/list/', UserListView.as_view(), name='user_list_alt'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/detail/<int:pk>/', UserDetailView.as_view(), name='user_detail_alt'),
    path('users/new/', UserCreateView.as_view(), name='user_create'),
    path('users/create/', UserCreateView.as_view(), name='user_create_alt'),
    path('users/add/', UserCreateView.as_view(), name='user_create_add'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update_alt'),
    path('users/<int:pk>/change/', UserUpdateView.as_view(), name='user_update_change'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('users/<int:pk>/remove/', UserDeleteView.as_view(), name='user_delete_alt'),
    path('users/<int:user_id>/profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),
]