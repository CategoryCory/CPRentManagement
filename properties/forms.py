from django.forms import ModelForm

from .models import Property


class PropertyForm(ModelForm):
    template_name = 'forms/form_snippet.html'

    class Meta:
        model = Property
        fields = [
            'date_built',
            'key_number',
            'description',
            'addr_line_1',
            'addr_line_2',
            'addr_city',
            'addr_state',
            'addr_zip',
            'property_type',
            'square_feet',
            'taxes',
            'insurance',
            'company',
        ]
