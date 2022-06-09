from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Property
from .forms import PropertyForm


class PropertyListView(LoginRequiredMixin, ListView):
    model = Property
    paginate_by = 25
    queryset = Property.objects.order_by('addr_city', 'addr_state', 'addr_zip', 'addr_line_1')


class PropertyDetailView(LoginRequiredMixin, DetailView):
    model = Property


class PropertyCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Property
    form_class = PropertyForm
    permission_required = ('properties.add_property', )
    permission_denied_message = 'You do not have sufficient privileges to add properties.'
    success_url = reverse_lazy('properties:property-list')
    success_message = 'Property successfully added.'


class PropertyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Property
    form_class = PropertyForm
    permission_required = ('properties.change_property', )
    permission_denied_message = 'You do not have sufficient privileges to edit properties.'
    success_url = reverse_lazy('properties:property-list')
    success_message = 'Property successfully updated.'
