from django.urls import path

from .views import UnitListView

app_name = 'units'
urlpatterns = [
    path('', UnitListView.as_view(), name='unit-list'),
]