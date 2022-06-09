from django import forms

from .models import Property


class PropertyForm(forms.ModelForm):
    template_name = 'forms/form_snippet.html'

    class Meta:
        model = Property
        fields = ('addr_line_1', 'addr_line_2', 'addr_city', 'addr_state', 'addr_zip', 'company',
            'description', 'property_type', 'key_number', 'date_built', 'square_feet', 'taxes',
            'insurance',
        )
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, }),
            'date_built': forms.TextInput(attrs={'type': 'date', })
        }
