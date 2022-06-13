from django import template

register = template.Library()


@register.inclusion_tag('form_input.html')
def form_input(field, num_cols):
    return {'field': field, 'num_cols': num_cols}


@register.inclusion_tag('form_checkbox.html')
def form_checkbox(field):
    return {'field': field}


@register.inclusion_tag('form_button_row.html')
def form_button_row(cancel_url):
    return {'cancel_url': cancel_url}
