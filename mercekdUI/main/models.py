from django.db import models

class Lease(models.Model):
     ip = models.CharField(null=True)
     mac = models.CharField(null=True)
     starts = models.DateTimeField(null=True)
     ends = models.DateTimeField(null=True)
     uid = models.CharField(null=True)
     client = models.CharField(null=True)
     def has_alias(self):
        if len(self.alias_set.all())!=0:
          return True
        else:
          return False
     def get_alias(self):
           return self.alias_set.all()[0]

class Alias(models.Model):
     lease = models.ForeignKey('Lease')
     mac_name = models.CharField(null=True)
     ip_name = models.CharField(null=True)

class LeasesFilePath(models.Model):
     path = models.CharField(null=True)

# Create your models here.
