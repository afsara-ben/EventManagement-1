from django.db import models


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255)
    vendor_email = models.CharField(max_length=255)
    vendor_password = models.CharField(max_length=255)
    vendor_company_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    vendor_company_website = models.CharField(max_length=255, default=None, blank=True, null=True)
    vendor_establish_time = models.IntegerField(default=None, blank=True, null=True)
    vendor_employee_number = models.IntegerField(default=None, blank=True, null=True)
    vendor_annual_turnover = models.IntegerField(default=None, blank=True, null=True)
    vendor_member_type = models.CharField(max_length=255, default=None, blank=True, null=True)
    vendor_remote_work = models.CharField(max_length=255, default=None, blank=True, null=True)
    vendor_description = models.CharField(max_length=2083, default=None, blank=True, null=True)
    vendor_logo = models.CharField(max_length=255, default=None, blank=True, null=True)

class Vendor_Info(models.Model):
    vendor_company_address = models.CharField(max_length=255, default=None, blank=True, null=True)
    vendor_contact_number = models.IntegerField(default=None, blank=True, null=True)
    vendor_social_media = models.CharField(max_length=255, default=None, blank=True, null=True)
    vendor_specialty = models.CharField(max_length=255, default=None, blank=True, null=True)
    vendor_past_work = models.CharField(max_length=2083, default=None, blank=True, null=True)
    vendor_upcoming_work = models.CharField(max_length=2083, default=None, blank=True, null=True)
    vendor_provide_design = models.CharField(max_length=2083, default=None, blank=True, null=True)
    vendor_company = models.ForeignKey('Vendor', on_delete=models.CASCADE)


class Service_type(models.Model):
    service_name = models.CharField(max_length=255)
    service_rate = models.FloatField
    service_quantity = models.IntegerField
    service_arrival_date = models.DateField
    service_arrival_time = models.TimeField
    vendor_company = models.ForeignKey('Vendor', on_delete=models.CASCADE)

