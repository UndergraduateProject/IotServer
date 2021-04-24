from django.db import models
from client.models import Client

# Create your models here.


class Sensor(models.Model):
<<<<<<< HEAD
    clientID = models.ForeignKey(Client, related_name='sensors', on_delete=models.CASCADE, null=True)
    sensorID = models.IntegerField(primary_key=True, auto_created=True)
    sensorName = models.CharField(max_length=30)
    
=======
    client = models.ForeignKey(
        Client, related_name="sensors", on_delete=models.CASCADE, null=True
    )
    sensorID = models.IntegerField(primary_key=True, auto_created=True)
    sensorName = models.CharField(max_length=30)

    def __str__(self):
        return self.sensorName

>>>>>>> a95922caf693df3b893fe09f64e6753bfd77a21c

class Humid_Temp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    humidity = models.FloatField()
    temperature = models.FloatField()
    heatIndex = models.FloatField(default=0)
    sensor = models.ForeignKey(
        Sensor, related_name="humid_temp", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return "humidity : %d , temperature : %d" % (self.humidity, self.temperature)


class Moisture(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    sensor = models.ForeignKey(
        Sensor, related_name="moisture", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.value
