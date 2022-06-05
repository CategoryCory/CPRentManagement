from django.contrib import admin

from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['full_address', 'square_feet', 'description', ]
    list_per_page = 25


admin.site.register(Property, PropertyAdmin)
