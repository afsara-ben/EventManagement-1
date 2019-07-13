from django.db import models


class Picture(models.Model):
    image_name = models.CharField(max_length=2080)
    image_file = models.ImageField(upload_to='images/')
    uploader = models.CharField(max_length=255, default=None, blank=True, null=True)

