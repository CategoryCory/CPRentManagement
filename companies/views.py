from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Company


class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    paginate_by: 25


class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company


class CompanyCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Company
    fields = [
        'company_name',
        'addr_line_1',
        'addr_line_2',
        'addr_city',
        'addr_state',
        'addr_zip',
        'phone',
        'alt_phone',
        'fax',
    ]
    permission_required = ('companies.add_company', )
    permission_denied_message = 'You do not have sufficient privileges to add companies.'
    success_url = reverse_lazy('companies:company-list')
    success_message = 'Company successfully added.'


class CompanyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Company
    fields = [
        'company_name',
        'addr_line_1',
        'addr_line_2',
        'addr_city',
        'addr_state',
        'addr_zip',
        'phone',
        'alt_phone',
        'fax',
    ]
    permission_required = ('companies.change_company', )
    permission_denied_message = 'You do not have sufficient privileges to edit companies.'
    success_url = reverse_lazy('companies:company-list')
    success_message = 'Company successfully edited.'
