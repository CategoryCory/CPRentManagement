from django.urls import path

from .views import UnitListView, UnitDetailView, UnitCreateView, UnitUpdateView

app_name = 'units'
urlpatterns = [
    path('', UnitListView.as_view(), name='unit-list'),
    path('add/', UnitCreateView.as_view(), name='unit-add'),
    path('<int:pk>/edit/', UnitUpdateView.as_view(), name='unit-edit'),
    path('<int:pk>/', UnitDetailView.as_view(), name='unit-detail'),
]
