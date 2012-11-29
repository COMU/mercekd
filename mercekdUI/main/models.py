from django.db import models

class Lease(models.Model):
     ip = models.ForeignKey('Lease_IP',null=True)
     mac = models.ForeignKey('Lease_Mac',null=True)
     starts = models.DateTimeField(null=True)
     ends = models.DateTimeField(null=True)
     uid = models.CharField(null=True)
     client = models.CharField(null=True)

class Lease_IP(models.Model):
     v4 = models.CharField(null=True)
     ip_name = models.CharField(null=True)

class Lease_Mac(models.Model):
     mac = models.CharField(null=True)
     mac_name = models.CharField(null=True)

class LeasesFilePath(models.Model):
     path = models.CharField(null=True)

# Create your models here.
