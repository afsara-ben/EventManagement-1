# Generated by Django 2.0.5 on 2019-07-12 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_name', models.CharField(max_length=255)),
                ('sponsor_email', models.CharField(max_length=255)),
                ('sponsor_password', models.CharField(max_length=255)),
                ('sponsor_address', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('sponsor_occupation', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('sponsor_work_website', models.CharField(blank=True, default=None, max_length=2083, null=True)),
                ('sponsor_company_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('sponsor_contact_number', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
