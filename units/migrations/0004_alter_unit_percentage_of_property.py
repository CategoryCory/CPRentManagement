# Generated by Django 4.0.5 on 2022-06-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0003_unit_calculate_tax_and_ins_unit_unit_insurance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='percentage_of_property',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
