# Generated by Django 4.0.5 on 2022-06-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0002_alter_unit_addr_line_1_alter_unit_addr_line_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='calculate_tax_and_ins',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='unit_insurance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AddField(
            model_name='unit',
            name='unit_taxes',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
