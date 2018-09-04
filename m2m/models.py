from django.db import models

# Create your models here.

class Boy(models.Model):
    bname = models.CharField(max_length=32)


class Girl(models.Model):
    gname = models.CharField(max_length=32)


class Love(models.Model):
    b = models.ForeignKey('Boy',on_delete=models.CASCADE)
    g = models.ForeignKey('Girl',on_delete=models.CASCADE)


