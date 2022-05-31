from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'full_address', 'phone', ]
    list_per_page = 10


admin.site.register(Company, CompanyAdmin)
