from django.contrib import admin

from .models import Tenant


class TenantAdmin(admin.ModelAdmin):
    list_display = ('contact_person', 'phone', 'email', 'move_in_date', 'move_out_date', 'unit', )
    list_per_page = 25
    list_editable = ('move_in_date', 'move_out_date', 'unit', )


admin.site.register(Tenant, TenantAdmin)
