# Generated by Django 3.2 on 2021-06-25 17:14

from django.db import migrations, models
import enviroment.models


class Migration(migrations.Migration):

    dependencies = [
        ('enviroment', '0005_plantimg_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantimg',
            name='img',
            field=models.ImageField(upload_to=enviroment.models.imghelper),
        ),
    ]
