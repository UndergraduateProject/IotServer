# Generated by Django 3.2 on 2021-07-03 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=512)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='controller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Watering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('controller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='watering', to='controller.controller')),
            ],
        ),
        migrations.CreateModel(
            name='LED',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red', models.FloatField()),
                ('green', models.FloatField()),
                ('blue', models.FloatField()),
                ('brightness', models.FloatField()),
                ('switch', models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF')], max_length=3)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('controller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='LED', to='controller.controller')),
            ],
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('switch', models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF')], max_length=3)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('controller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fan', to='controller.controller')),
            ],
        ),
    ]
