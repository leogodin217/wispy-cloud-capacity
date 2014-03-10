from django.db import models

# Create your models here.


class VirtualEnvironment(models.Model):
    """Represents a grouping of related clusters.
    """

    name = models.CharField(max_length=100, default="ve1")
    market = models.CharField(max_length=64, default="DCU")
    site = models.CharField(max_length=64, default="Folsom")
    segment = models.CharField(max_length=64, default="Internal")
    application_layer = models.CharField(max_length=64, default="General")
    pipe = models.CharField(max_length=64, default="General")
    notes = models.TextField(default="")
    status = models.CharField(max_length=64, default="Available")
