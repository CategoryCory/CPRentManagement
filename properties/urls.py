from django.urls import path

from .views import PropertyListView, PropertyDetailView, PropertyCreateView, PropertyUpdateView

app_name = 'properties'
urlpatterns = [
    path('', PropertyListView.as_view(), name='property-list'),
    path('add/', PropertyCreateView.as_view(), name='property-add'),
    path('<int:pk>/edit/', PropertyUpdateView.as_view(), name='property-edit'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
]