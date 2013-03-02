from django.db import models

class Lease(models.Model):
     ip = models.ForeignKey('Lease_IP',null=True)
     mac = models.ForeignKey('Lease_Mac',null=True)
     starts = models.DateTimeField(null=True,max_length=0)
     ends = models.DateTimeField(null=True)
     uid = models.TextField(null=True)
     client = models.TextField(null=True)

class Lease_IP(models.Model):
     v4 = models.TextField(null=True)
     ip_name = models.TextField(null=True)

class Lease_Mac(models.Model):
     mac = models.TextField(null=True)
     mac_name = models.TextField(null=True)

class LeasesFilePath(models.Model):
     path = models.TextField(null=True)

class Subnet(models.Model):
     ip = models.TextField(null=True)
     mask = models.TextField(null=True)
     alias = models.TextField(null=True)
     
# Create your models here.
