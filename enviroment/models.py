from django.db import models

# Create your models here.


class Humidity(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    sensorId = models.CharField(max_length=10, default='none')


class Temperature(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    sensorId = models.CharField(max_length=10, default='none')
