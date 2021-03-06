from functools import partial
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
    timestamp = instance.timestamp + timedelta(hours=8)
    if 'RAW' in filename:
        return timestamp.strftime('%Y/')+timestamp.strftime('%m%d/')+timestamp.strftime('%H:%M:%S_YOLO')+'.jpg'
    return timestamp.strftime('%Y/')+timestamp.strftime('%m%d/')+timestamp.strftime('%H:%M:%S_RAW')+'.jpg'

class PlantImg(models.Model):
    sensor = models.ForeignKey(Sensor, related_name="plantimg", on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=imghelper)
    yolo_image = models.ImageField(upload_to=imghelper, null=True, blank=True)

    def __str__(self):
        return str(self.timestamp.astimezone(timezone(timedelta(hours=8))))


def plantimgcrophelper(instance, filename):
    timestamp = instance.plantimg.timestamp + timedelta(hours=8)
    if 'cam++' in filename:
        return timestamp.strftime('%Y/')+timestamp.strftime('%m%d/')+timestamp.strftime('%H%M%S_crop/')+'cam++'+filename.split('/')[-1]
    return timestamp.strftime('%Y/')+timestamp.strftime('%m%d/')+timestamp.strftime('%H%M%S_crop/')+filename.split('/')[-1]

class PlantYoloCropImg(models.Model):
    plantimg = models.ForeignKey(PlantImg, related_name="plant_yolo_crop", on_delete=models.CASCADE)
    prob = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=plantimgcrophelper)
    gradcam_image = models.ImageField(upload_to=plantimgcrophelper)

    def __str__(self):
        return str(self.timestamp.astimezone(timezone(timedelta(hours=8))))