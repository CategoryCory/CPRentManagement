from django.db import models


class ChargeAccount(models.Model):
    name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
