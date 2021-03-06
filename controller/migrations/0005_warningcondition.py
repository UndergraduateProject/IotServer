# Generated by Django 3.2 on 2021-07-14 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('controller', '0004_alter_actioncondition_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarningCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moisture', models.FloatField()),
                ('humidity', models.FloatField()),
                ('temperature', models.FloatField()),
                ('operator', models.CharField(choices=[('<', '<'), ('>', '<')], max_length=1)),
                ('status', models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF')], max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='warning_condition', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
