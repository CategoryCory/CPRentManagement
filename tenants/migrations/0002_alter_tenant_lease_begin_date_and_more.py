# Generated by Django 4.0.5 on 2022-06-10 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='lease_begin_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='lease_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='move_in_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='move_out_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
