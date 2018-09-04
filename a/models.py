from django.db import models


# Create your models here.


class Host(models.Model):
    hid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32)
    ip = models.GenericIPAddressField(protocol='ipv4', db_index=True)
    port = models.IntegerField()


class App(models.Model):
    aid = models.AutoField(primary_key=True)
    appname = models.CharField(max_length=32)
    h_a = models.ManyToManyField('Host')


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.IntegerField()


class UserGroup(models.Model):
    gid = models.AutoField(primary_key=True)
    groupname = models.CharField(max_length=32)
    ug_u = models.ManyToManyField('User')
    # ug_h = models.ForeignKey(to='Host',to_field='hid',on_delete=models.CASCADE)
