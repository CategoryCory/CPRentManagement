# Generated by Django 4.0.5 on 2022-06-10 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('units', '0004_alter_unit_percentage_of_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=25)),
                ('work_phone', models.CharField(blank=True, max_length=25)),
                ('cell_phone', models.CharField(blank=True, max_length=25)),
                ('fax', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('date_of_birth', models.DateField(blank=True)),
                ('ssn', models.CharField(blank=True, max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=50)),
                ('alternate_company_1', models.CharField(blank=True, max_length=50, verbose_name='Alternate company name')),
                ('alternate_company_2', models.CharField(blank=True, max_length=50, verbose_name='Alternate company name 2')),
                ('addr_line_1', models.CharField(max_length=100, verbose_name='Address line 1')),
                ('addr_line_2', models.CharField(blank=True, max_length=100, verbose_name='Address line 2')),
                ('addr_city', models.CharField(max_length=50, verbose_name='City')),
                ('addr_state', models.CharField(max_length=25, verbose_name='State')),
                ('addr_zip', models.CharField(max_length=20, verbose_name='Zip code')),
                ('notes', models.TextField(blank=True)),
                ('move_in_date', models.DateField(blank=True)),
                ('move_out_date', models.DateField(blank=True)),
                ('lease_begin_date', models.DateField(blank=True)),
                ('lease_end_date', models.DateField(blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='units.unit')),
            ],
        ),
    ]
