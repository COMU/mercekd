from django.db import models
class lease_db(models.Model):
    ip=models.IPAddressField(blank=False)
    mac=models.CharField(max_length=20,blank=False)
    start=models.DateTimeField(blank=False)
    end=models.DateTimeField(blank=False)
    uid=models.CharField(max_length=100,blank=True)
    client=models.CharField(max_length=100,blank=True)

    class Meta:
        db_table="lease_db"