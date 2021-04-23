from django.db import models
from client.models import Client

# Create your models here.


class Sensor(models.Model):
    clientID = models.ForeignKey(Client, related_name='sensors', on_delete=models.CASCADE, null=True)
    sensorID = models.IntegerField(primary_key=True, auto_created=True)
    sensorName = models.CharField(max_length=30)
    

class Humid_Temp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    humidity = models.FloatField()
    temperature = models.FloatField()
    heatIndex = models.FloatField(default=0)
    # sensorID = models.ForeignKey(Sensor, on_delete=models.CASCADE)


class Moisture(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    # sensorID = models.ForeignKey(Sensor, on_delete=models.CASCADE)
