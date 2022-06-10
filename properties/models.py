from django.db import models
from django.urls import reverse

from companies.models import Company


class Property(models.Model):
    COMMERCIAL = 'commercial'
    RESIDENTIAL = 'residential'
    BILLBOARD = 'billboard'
    TOWER = 'tower'

    PROPERTY_TYPE_CHOICES = (
        (COMMERCIAL, 'Commercial'),
        (RESIDENTIAL, 'Residential'),
        (BILLBOARD, 'Billboard'),
        (TOWER, 'Tower'),
    )

    date_built = models.DateField(null=True, blank=True, verbose_name='Date Built')
    key_number = models.IntegerField(null=True, blank=True, verbose_name='Key Number')
    description = models.TextField(blank=True, verbose_name='Description/Notes')
    addr_line_1 = models.CharField(max_length=100, verbose_name='Address Line 1')
    addr_line_2 = models.CharField(max_length=100, blank=True, verbose_name='Address Line 2')
    addr_city = models.CharField(max_length=50, verbose_name='City')
    addr_state = models.CharField(max_length=25, verbose_name='State')
    addr_zip = models.CharField(max_length=20, verbose_name='Zip Code')
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default=COMMERCIAL,
                                     verbose_name='Property Type')
    square_feet = models.IntegerField(default=0)
    taxes = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    insurance = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def full_address(self):
        return f'{self.addr_line_1}, {self.addr_city}, {self.addr_state} {self.addr_zip}'

    def save(self, *args, **kwargs):
        # Update percentage of square feet on all units in this property
        if self.square_feet != 0:
            subunits = self.unit_set.all()

            for u in subunits:
                if u.calculate_tax_and_ins is True:
                    u.save()

        super(Property, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_address

    def get_absolute_url(self):
        return reverse('properties:property-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Properties'
