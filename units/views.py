from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Unit
from .forms import UnitForm


class UnitListView(LoginRequiredMixin, ListView):
    model = Unit
    paginate_by = 25
    queryset = Unit.objects.order_by('addr_line_1')


class UnitDetailView(LoginRequiredMixin, DetailView):
    model = Unit


class UnitCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Unit
    form_class = UnitForm
    permission_required = ('units.add_unit', )
    permission_denied_message = 'You do not have sufficient privileges to add units.'
    success_url = reverse_lazy('units:unit-list')
    success_message = 'Unit successfully added.'


class UnitUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Unit
    form_class = UnitForm
    permission_required = ('units.change_unit', )
    permission_denied_message = 'You do not have sufficient privileges to edit units.'
    success_url = reverse_lazy('units:unit-list')
    success_message = 'Unit successfully updated.'
