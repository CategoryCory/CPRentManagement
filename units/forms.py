from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Unit


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('addr_line_1', 'addr_line_2', 'parent_property', 'unit_status', 'square_feet', 'rent', 'unit_taxes',
                  'unit_insurance', 'calculate_tax_and_ins', )
        labels = {
            'calculate_tax_and_ins': _('Calculate taxes and insurance from square feet?')
        }
