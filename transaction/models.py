from django.db import models


class AdminAgency_Transaction(models.Model):
    admin_agency_amount = models.IntegerField
    admin_agency_date = models.DateField
    admin_agency_time = models.TimeField
    admin_agency_pay_method = models.CharField(max_length=255)
    admin_agency_pay_status = models.CharField(max_length=255)
    agency = models.ForeignKey('agency.Agency', on_delete=models.CASCADE, default=None, blank=True, null=True)


class ClientAgency_Transaction(models.Model):
    client_agency_amount = models.IntegerField
    client_agency_date = models.DateField
    client_agency_time = models.TimeField
    client_agency_pay_method = models.CharField(max_length=255)
    client_agency_pay_status = models.CharField(max_length=255)
    agency = models.ForeignKey('agency.Agency', on_delete=models.CASCADE, default=None, blank=True, null=True)
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, default=None, blank=True, null=True)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, default=None, blank=True, null=True)


class ClientService_Transaction(models.Model):
    client_service_amount = models.IntegerField
    client_service_date = models.DateField
    client_service_time = models.TimeField
    client_service_pay_method = models.CharField(max_length=255)
    client_service_pay_status = models.CharField(max_length=255)
    vendor = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE, default=None, blank=True, null=True)
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, default=None, blank=True, null=True)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, default=None, blank=True, null=True)

