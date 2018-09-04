from django.db import models

# Create your models here.

class Bussiness(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32,default=1,null=True)


class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(protocol='ipv4',db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey(to='Bussiness',to_field='id',on_delete=models.CASCADE)




class Application(models.Model):
    name = models.CharField(max_length=32)
    r = models.ManyToManyField("Host")


