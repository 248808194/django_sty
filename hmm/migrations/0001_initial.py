# Generated by Django 2.0.5 on 2018-06-04 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('groupname', models.CharField(max_length=64)),
                ('gid', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('user_group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hmm.group')),
            ],
        ),
    ]
