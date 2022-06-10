from django.db import models
from django.urls import reverse

from decimal import Decimal

from properties.models import Property


class Unit(models.Model):
    OCCUPIED = 'occupied'
    AVAILABLE = 'available'

    UNIT_AVAILABILITY_CHOICES = (
        (OCCUPIED, 'Occupied'),
        (AVAILABLE, 'Available'),
    )

    addr_line_1 = models.CharField(max_length=100, verbose_name='Address Line 1')
    addr_line_2 = models.CharField(max_length=100, blank=True, verbose_name='Address Line 2')
    rent = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    square_feet = models.IntegerField(default=0)
    percentage_of_property = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    unit_status = models.TextField(max_length=20,
                                   choices=UNIT_AVAILABILITY_CHOICES,
                                   default=AVAILABLE,
                                   verbose_name='Unit Availability')
    unit_taxes = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    unit_insurance = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    calculate_tax_and_ins = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    parent_property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate and save percentage_of_property
        if self.parent_property is not None:
            parent_sq_footage = self.parent_property.square_feet

            if parent_sq_footage != 0 and self.square_feet != 0:
                self.percentage_of_property = Decimal(self.square_feet) / Decimal(parent_sq_footage)

                # If calculate_tax_and_ins is true, then calculate unit taxes and insurance
                if self.calculate_tax_and_ins is True:
                    parent_taxes = self.parent_property.taxes
                    parent_insurance = self.parent_property.insurance

                    if parent_taxes != 0.0:
                        self.unit_taxes = Decimal(parent_taxes) * Decimal(self.percentage_of_property)

                    if parent_insurance != 0.0:
                        self.unit_insurance = Decimal(parent_insurance) * Decimal(self.percentage_of_property)

        super(Unit, self).save(*args, **kwargs)

    def __str__(self):
        return self.addr_line_1
    
    def get_absolute_url(self):
        return reverse('units:unit-detail', kwargs={'pk': self.pk})
