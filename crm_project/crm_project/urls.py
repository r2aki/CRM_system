from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),
    path('dashboard/', DashboardView.as_view(), name='dashboard_alt'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('ads/', include('ads.urls')),
    path('leads/', include('leads.urls')),
    path('customers/', include('customers.urls')),
    path('contracts/', include('contracts.urls')),
    path('registration/', include('registration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)