from django.db import models
from django.urls import reverse


class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True, verbose_name='Company Name')
    addr_line_1 = models.CharField(max_length=50, verbose_name='Address Line 1')
    addr_line_2 = models.CharField(max_length=50, blank=True, verbose_name='Address Line 2')
    addr_city = models.CharField(max_length=50, verbose_name='City')
    addr_state = models.CharField(max_length=25, verbose_name='State')
    addr_zip = models.CharField(max_length=15, verbose_name='Zip Code')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    alt_phone = models.CharField(max_length=20, blank=True, verbose_name='Alternate Phone')
    fax = models.CharField(max_length=20, blank=True, verbose_name='Fax')
    is_deleted = models.BooleanField(default=False)

    @property
    def full_address(self):
        return f'{self.addr_line_1}, {self.addr_city}, {self.addr_state} {self.addr_zip}'

    def __str__(self) -> str:
        return self.company_name
    
    def get_absolute_url(self):
        return reverse('companies:company-detail', kwargs={"pk": self.pk})
    

    class Meta:
        verbose_name_plural = 'Companies'
