# Generated by Django 2.0.5 on 2018-06-08 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='ug_u',
            field=models.ManyToManyField(to='a.User'),
        ),
    ]
