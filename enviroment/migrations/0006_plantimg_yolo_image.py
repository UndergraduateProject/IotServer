# Generated by Django 3.2 on 2021-07-14 11:26

from django.db import migrations, models
import enviroment.models


class Migration(migrations.Migration):

    dependencies = [
        ('enviroment', '0005_plantyolocropimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantimg',
            name='yolo_image',
            field=models.ImageField(blank=True, null=True, upload_to=enviroment.models.imghelper),
        ),
    ]
