from django.db import models
from datetime import timedelta, timezone

class Sensor(models.Model):
    user = models.ForeignKey('auth.User', related_name ='sensor', on_delete=models.PROTECT)
    name = models.CharField(primary_key=True, max_length=128)
    description = models.CharField(blank=True, max_length=512)
    interval = models.DurationField(default=timedelta(seconds=30))
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class HumidTemp(models.Model):
    sensor = models.ForeignKey(Sensor, related_name="humidtemp", on_delete=models.PROTECT)
    humidity = models.FloatField()
    temperature = models.FloatField()
    heatIndex = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.timestamp.astimezone(timezone(timedelta(hours=8))))


class Moisture(models.Model):
    sensor = models.ForeignKey(Sensor, related_name="moisture", on_delete=models.PROTECT)
    moisture = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.timestamp.astimezone(timezone(timedelta(hours=8))))

def imghelper(instance, filename):
    return instance.created.strftime('%Y/')+instance.created.strftime('%m%d/')+instance.created.strftime('%H%M')+'.jpg'

class PlantImg(models.Model):
    sensor = models.ForeignKey(Sensor, related_name="plantimg", on_delete=models.PROTECT)
    image = models.ImageField(upload_to=imghelper)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.timestamp.astimezone(timezone(timedelta(hours=8))))