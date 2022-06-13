from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Tenant


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ('contact_person', 'phone', 'work_phone', 'cell_phone', 'fax', 'email', 'date_of_birth', 'ssn',
                  'company_name', 'alternate_company_1', 'alternate_company_2', 'addr_line_1', 'addr_line_2',
                  'addr_city', 'addr_state', 'addr_zip', 'notes', 'move_in_date', 'move_out_date',
                  'lease_begin_date', 'lease_end_date', 'unit', )
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4, }),
            'date_of_birth': forms.TextInput(attrs={'type': 'date', }),
            'move_in_date': forms.TextInput(attrs={'type': 'date', }),
            'move_out_date': forms.TextInput(attrs={'type': 'date', }),
            'lease_begin_date': forms.TextInput(attrs={'type': 'date', }),
            'lease_end_date': forms.TextInput(attrs={'type': 'date', }),
        }
        labels = {
            'ssn': _('Social security number'),
        }
