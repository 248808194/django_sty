from django.db import models

# Create your models here.


class group(models.Model):

    groupname = models.CharField(max_length=64)
    gid = models.AutoField(primary_key=True)


class userinfo(models.Model):

    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    uid = models.AutoField(primary_key=True)
    user_group = models.ForeignKey('group',to_field='gid',default=1,on_delete=models.CASCADE,related_name='bvv') #relasted_name =b  查询的时候 b等同于 XXOO_set