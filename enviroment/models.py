from django.db import models
#from django.contrib.auth.models import User
# Create your models here.


class Sensor(models.Model):
    user = models.ForeignKey('auth.User', related_name ='sensors', on_delete=models.CASCADE)
    sensorName = models.CharField(max_length=30)

    def __str__(self):
        return self.sensorName


class Humid_Temp(models.Model):
    sensor = models.ForeignKey(Sensor, related_name="humid_temp", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    humidity = models.FloatField()
    temperature = models.FloatField()
    heatIndex = models.FloatField(default=0)

    def __str__(self):
        return "humidity : %d , temperature : %d" % (self.humidity, self.temperature)


class Moisture(models.Model):
    sensor = models.ForeignKey(Sensor, related_name="moisture", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    
    def __str__(self):
        return str(self.value)
