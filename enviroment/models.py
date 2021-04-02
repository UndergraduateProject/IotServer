from django.db import models

# Create your models here.


class Humidity(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()


class Temperature(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
