# Generated by Django 4.0.5 on 2022-06-10 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0002_alter_tenant_lease_begin_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
