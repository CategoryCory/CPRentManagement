from django.db import models
from django.urls import reverse

from units.models import Unit


class Tenant(models.Model):
    contact_person = models.CharField(max_length=100)
    phone = models.CharField(max_length=25, blank=True)
    work_phone = models.CharField(max_length=25, blank=True)
    cell_phone = models.CharField(max_length=25, blank=True)
    fax = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    date_of_birth = models.DateField(blank=True)
    ssn = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=50, blank=True)
    alternate_company_1 = models.CharField(max_length=50, blank=True, verbose_name='Alternate company name')
    alternate_company_2 = models.CharField(max_length=50, blank=True, verbose_name='Alternate company name 2')
    addr_line_1 = models.CharField(max_length=100, verbose_name='Address line 1')
    addr_line_2 = models.CharField(max_length=100, blank=True, verbose_name='Address line 2')
    addr_city = models.CharField(max_length=50, verbose_name='City')
    addr_state = models.CharField(max_length=25, verbose_name='State')
    addr_zip = models.CharField(max_length=20, verbose_name='Zip code')
    notes = models.TextField(blank=True)
    move_in_date = models.DateField(null=True, blank=True)
    move_out_date = models.DateField(null=True, blank=True)
    lease_begin_date = models.DateField(null=True, blank=True)
    lease_end_date = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.contact_person

    def get_absolute_url(self):
        return reverse('tenants:tenant-detail', kwargs={'pk': self.pk})
