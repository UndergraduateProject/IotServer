# Generated by Django 3.1.7 on 2021-04-21 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enviroment', '0002_auto_20210422_0153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='humid_temp',
            old_name='sensorID',
            new_name='sensor',
        ),
        migrations.RenameField(
            model_name='moisture',
            old_name='sensorID',
            new_name='sensor',
        ),
        migrations.RenameField(
            model_name='sensor',
            old_name='clientID',
            new_name='client',
        ),
    ]
