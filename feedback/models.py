from django.db import models


class Feedback(models.Model):
    customer_name = models.CharField(max_length=120, default=None, blank=True, null=True)
    email = models.EmailField(max_length=255, default=None, blank=True, null=True)
    details = models.TextField(default=None, blank=True, null=True)
    happy = models.FloatField(default=None, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name

