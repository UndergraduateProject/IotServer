# Generated by Django 3.2 on 2021-10-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0012_actioncondition_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='warningcondition',
            name='volume',
            field=models.FloatField(default=-1),
        ),
    ]