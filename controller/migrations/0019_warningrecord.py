# Generated by Django 3.2 on 2021-10-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0018_usertoplant'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarningRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]