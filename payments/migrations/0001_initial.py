# Generated by Django 4.0.5 on 2022-06-13 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenants', '0003_alter_tenant_date_of_birth'),
        ('charges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('t_payment', 'Payment'), ('t_credit', 'Credit'), ('t_deposit', 'Deposit')], default='t_payment', max_length=25)),
                ('payment_method', models.CharField(choices=[('check', 'Check'), ('cash', 'Cash'), ('credit_card', 'Credit Card'), ('electronic', 'Electronic')], default='check', max_length=25)),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('memo', models.CharField(blank=True, max_length=150)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tenants.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='ChargePaymentLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('charge', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='charges.charge')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='payments.payment')),
            ],
        ),
    ]
