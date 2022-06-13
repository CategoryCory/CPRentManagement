from django.db import models

from charge_accounts.models import ChargeAccount
from tenants.models import Tenant


class Charge(models.Model):
    PAID = 'paid'
    UNPAID = 'unpaid'
    LATE = 'late'

    CHARGE_STATUS_CHOICES = (
        (PAID, 'Paid'),
        (UNPAID, 'Unpaid'),
        (LATE, 'Late'),
    )

    charge_status = models.CharField(max_length=25, choices=CHARGE_STATUS_CHOICES, default=UNPAID)
    is_late_charge = models.BooleanField(default=False)
    charge_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    memo = models.CharField(max_length=150, blank=True)
    charge_account = models.ForeignKey(ChargeAccount, on_delete=models.SET_NULL, null=True, blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.RESTRICT)
    parent_charge = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent_charges')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(null=True, blank=True)
