# Generated by Django 3.2 on 2021-10-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0011_auto_20210929_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='actioncondition',
            name='volume',
            field=models.FloatField(default=-1),
        ),
    ]