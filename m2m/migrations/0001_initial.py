# Generated by Django 2.0.5 on 2018-06-11 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Girl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Love',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m2m.Boy')),
                ('g', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m2m.Girl')),
            ],
        ),
    ]