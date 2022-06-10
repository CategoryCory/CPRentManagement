from django import forms

from .models import Unit


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('addr_line_1', 'addr_line_2', 'parent_property', 'unit_status', 'square_feet', 'rent', )
