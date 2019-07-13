# Generated by Django 2.0.5 on 2019-07-12 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('client_email', models.CharField(max_length=255)),
                ('client_password', models.CharField(max_length=255)),
                ('client_address', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('client_occupation', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('client_work_website', models.CharField(blank=True, default=None, max_length=2083, null=True)),
                ('client_company_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('client_contact_number', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
