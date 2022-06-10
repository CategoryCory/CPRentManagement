from django.views.generic import ListView

from .models import Unit


class UnitListView(ListView):
    model = Unit
    paginate_by = 25
    queryset = Unit.objects.order_by('addr_line_1')
