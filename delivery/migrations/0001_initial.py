# Generated by Django 2.0.5 on 2019-07-12 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        ('agency', '0001_initial'),
        ('vendor', '0001_initial'),
        ('sponsor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorAgency_Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_agency_pay_method', models.CharField(max_length=255)),
                ('sponsor_agency_pay_status', models.CharField(max_length=255)),
                ('agency', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='agency.Agency')),
                ('event', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('sponsor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='sponsor.Sponsor')),
            ],
        ),
        migrations.CreateModel(
            name='VendorAgency_Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_agency_pay_method', models.CharField(max_length=255)),
                ('vendor_agency_pay_status', models.CharField(max_length=255)),
                ('agency', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='agency.Agency')),
                ('event', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('vendor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.Vendor')),
                ('vendor_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.Service_type')),
            ],
        ),
    ]
