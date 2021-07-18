# Generated by Django 3.2 on 2021-07-17 17:40

from django.db import migrations, models
import django.utils.timezone
import enviroment.models


class Migration(migrations.Migration):

    dependencies = [
        ('enviroment', '0006_plantimg_yolo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantyolocropimg',
            name='gradcam_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=enviroment.models.plantimgcrophelper),
            preserve_default=False,
        ),
    ]
