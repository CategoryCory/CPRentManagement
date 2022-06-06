from django.urls import path

from .views import PropertyListView, PropertyDetailView, PropertyCreateView, PropertyUpdateView

app_name = 'properties'
urlpatterns = [
    path('', PropertyListView.as_view(), name='property-list'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
    path('add/', PropertyCreateView.as_view(), name='property-add'),
    path('edit/<int:pk>/', PropertyUpdateView.as_view(), name='property-edit'),
]