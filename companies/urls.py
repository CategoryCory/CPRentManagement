from django.urls import path

from .views import CompanyListView, CompanyDetailView, CompanyCreateView, CompanyUpdateView

app_name = 'companies'
urlpatterns = [
    path('', CompanyListView.as_view(), name='company-list'),
    path('add/', CompanyCreateView.as_view(), name='company-add'),
    path('<int:pk>/edit/', CompanyUpdateView.as_view(), name='company-edit'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
]
