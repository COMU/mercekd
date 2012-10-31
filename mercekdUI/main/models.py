from django.db import models

class Lease(models.Model):
     ip = models.CharField(null=True)
     mac = models.CharField(null=True)
     starts = models.DateTimeField(null=True)
     ends = models.DateTimeField(null=True)
     uid = models.CharField(null=True)
     client = models.CharField(null=True)

# Create your models here.
