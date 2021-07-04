# Generated by Django 3.2 on 2021-07-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0002_actioncondition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actioncondition',
            name='volumne',
        ),
        migrations.AddField(
            model_name='actioncondition',
            name='volume',
            field=models.FloatField(default=-1),
        ),
        migrations.AlterField(
            model_name='actioncondition',
            name='moisture',
            field=models.FloatField(default=-1),
        ),
        migrations.AlterField(
            model_name='actioncondition',
            name='temperature',
            field=models.FloatField(default=-1),
        ),
    ]