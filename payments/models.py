from django.db import models

from charges.models import Charge
from tenants.models import Tenant


class Payment(models.Model):
    T_PAYMENT = 't_payment'
    T_CREDIT = 't_credit'
    T_DEPOSIT = 't_deposit'

    CHECK = 'check'
    CASH = 'cash'
    CREDIT_CARD = 'credit_card'
    ELECTRONIC = 'electronic'

    PAYMENT_TYPE_CHOICES = (
        (T_PAYMENT, 'Payment'),
        (T_CREDIT, 'Credit'),
        (T_DEPOSIT, 'Deposit'),
    )

    PAYMENT_METHOD_CHOICES = (
        (CHECK, 'Check'),
        (CASH, 'Cash'),
        (CREDIT_CARD, 'Credit Card'),
        (ELECTRONIC, 'Electronic'),
    )

    payment_type = models.CharField(max_length=25, choices=PAYMENT_TYPE_CHOICES, default=T_PAYMENT)
    payment_method = models.CharField(max_length=25, choices=PAYMENT_METHOD_CHOICES, default=CHECK)
    payment_date = models.DateTimeField(null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    memo = models.CharField(max_length=150, blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.RESTRICT)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(null=True, blank=True)


class ChargePaymentLink(models.Model):
    charge = models.ForeignKey(Charge, on_delete=models.RESTRICT)
    payment = models.ForeignKey(Payment, on_delete=models.RESTRICT)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(null=True, blank=True)
