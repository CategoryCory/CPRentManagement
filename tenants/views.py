from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Tenant
from .forms import TenantForm


class TenantListView(LoginRequiredMixin, ListView):
    model = Tenant
    paginate_by = 25
    queryset = Tenant.objects.order_by('contact_person', )


class TenantDetailView(LoginRequiredMixin, DetailView):
    model = Tenant


class TenantCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tenant
    form_class = TenantForm
    permission_required = ('tenants.add_tenant', )
    permission_denied_message = 'You do not have sufficient privileges to add tenants.'
    success_url = reverse_lazy('tenants:tenant-list')
    success_message = 'Tenant successfully added.'


class TenantUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tenant
    form_class = TenantForm
    permission_required = ('tenants.change_tenant', )
    permission_denied_message = 'You do not have sufficient privileges to edit tenants.'
    success_url = reverse_lazy('tenants:tenant-list')
    success_message = 'Tenant successfully updated.'
