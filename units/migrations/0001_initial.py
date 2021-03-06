# Generated by Django 4.0.4 on 2022-06-09 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0006_alter_property_taxes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr_line_1', models.TextField(max_length=100, verbose_name='Address Line 1')),
                ('addr_line_2', models.TextField(blank=True, max_length=100, verbose_name='Address Line 2')),
                ('rent', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('square_feet', models.IntegerField(default=0)),
                ('percentage_of_property', models.FloatField(default=0.0)),
                ('unit_status', models.TextField(choices=[('occupied', 'Occupied'), ('available', 'Available')], default='available', max_length=20, verbose_name='Unit Availability')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('parent_property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.property')),
            ],
        ),
    ]
