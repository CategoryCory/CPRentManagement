from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Company
from .forms import CompanyForm


class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    paginate_by: 25


class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company


class CompanyCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Company
    form_class = CompanyForm
    permission_required = ('companies.add_company', )
    permission_denied_message = 'You do not have sufficient privileges to add companies.'
    success_url = reverse_lazy('companies:company-list')
    success_message = 'Company successfully added.'


class CompanyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    permission_required = ('companies.change_company', )
    permission_denied_message = 'You do not have sufficient privileges to edit companies.'
    success_url = reverse_lazy('companies:company-list')
    success_message = 'Company successfully updated.'
