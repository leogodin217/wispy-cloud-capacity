from django.db import models

# Create your models here.

class VirtualEnvironment(models.Model):
    name = models.CharField(max_length=100)