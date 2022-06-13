from django.urls import path

from .views import TenantListView, TenantDetailView, TenantCreateView, TenantUpdateView

app_name = 'tenants'
urlpatterns = [
    path('', TenantListView.as_view(), name='tenant-list'),
    path('add/', TenantCreateView.as_view(), name='tenant-add'),
    path('<int:pk>/edit/', TenantUpdateView.as_view(), name='tenant-edit'),
    path('<int:pk>/', TenantDetailView.as_view(), name='tenant-detail'),
]