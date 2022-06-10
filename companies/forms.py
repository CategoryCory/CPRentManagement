from django.forms import ModelForm

from .models import Company


class CompanyForm(ModelForm):
    template_name = 'forms/form_snippet.html'

    class Meta:
        model = Company
        fields = ('company_name', 'addr_line_1', 'addr_line_2', 'addr_city', 'addr_state', 'addr_zip', 'phone',
                  'alt_phone', 'fax',)
