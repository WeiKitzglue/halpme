from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Point(models.Model):

    lat = models.FloatField()
    long = models.FloatField()
    time = models.DateTimeField(default=datetime.now, blank=True)