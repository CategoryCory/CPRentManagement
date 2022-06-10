from django.db import models
from django.urls import reverse

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
    percentage_of_property = models.FloatField(default=0.0)
    unit_status = models.TextField(max_length=20,
                                   choices=UNIT_AVAILABILITY_CHOICES,
                                   default=AVAILABLE,
                                   verbose_name='Unit Availability')
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    parent_property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Unit, self).save(*args, **kwargs)

    def __str__(self):
        return self.addr_line_1
    
    def get_absolute_url(self):
        return reverse('units:unit-detail', kwargs={'pk': self.pk})
