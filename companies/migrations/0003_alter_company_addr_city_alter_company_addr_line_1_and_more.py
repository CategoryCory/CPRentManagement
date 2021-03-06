# Generated by Django 4.0.4 on 2022-05-31 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_company_addr_line_2_alter_company_alt_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='addr_city',
            field=models.CharField(max_length=50, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='company',
            name='addr_line_1',
            field=models.CharField(max_length=50, verbose_name='Address Line 1'),
        ),
        migrations.AlterField(
            model_name='company',
            name='addr_line_2',
            field=models.CharField(blank=True, max_length=50, verbose_name='Address Line 2'),
        ),
        migrations.AlterField(
            model_name='company',
            name='addr_state',
            field=models.CharField(max_length=25, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='company',
            name='addr_zip',
            field=models.CharField(max_length=15, verbose_name='Zip Code'),
        ),
        migrations.AlterField(
            model_name='company',
            name='alt_phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Alternate Phone'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='fax',
            field=models.CharField(blank=True, max_length=20, verbose_name='Fax'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Phone'),
        ),
    ]
