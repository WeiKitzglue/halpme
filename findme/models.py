from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Point(models.Model):
    phone_no = models.CharField(max_length=12)
    lat = models.FloatField()
    lon = models.FloatField()
    time = models.DateTimeField(default=datetime.now, blank=True)
