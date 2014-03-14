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

    @property
    def name(self):
        return(self.market + ' ' +
               self.site + ' ' +
               self.segment + ' ' +
               self.application_layer + ' ' +
               self.pipe)

    def __unicode__(self):
        return self.name


class Cluster(models.Model):
    """Represents a single grouping of hypervisors
    """

    name = models.CharField(max_length=100, default="cluster1")
    notes = models.TextField(default="N/A")
    status = models.CharField(max_length=100, default="Open")
    virtual_environment = models.ForeignKey(VirtualEnvironment)

    def __unicode__(self):
        return self.name
