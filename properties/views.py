from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Property


class PropertyListView(LoginRequiredMixin, ListView):
    model = Property
    paginate_by = 25
