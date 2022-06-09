from django.contrib import admin

from .models import Unit


class UnitAdmin(admin.ModelAdmin):
    list_display = ('addr_line_1', 'rent', 'unit_status', 'parent_property', )
    list_editable = ('rent', 'unit_status', )
    list_per_page = 25


admin.site.register(Unit, UnitAdmin)
