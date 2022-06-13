from django import template

register = template.Library()


@register.inclusion_tag('form_field.html')
def form_field_template(field, num_cols):
    return {'field': field, 'num_cols': num_cols}


@register.inclusion_tag('form_button_row.html')
def form_button_row(cancel_url):
    return {'cancel_url': cancel_url}
