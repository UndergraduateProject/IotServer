from django.db import models
#from django.contrib.auth.models import User

class Sensor(models.Model):
    user = models.ForeignKey('auth.User', related_name ='sensor', on_delete=models.CASCADE)
    name = models.CharField(primary_key=True, max_length=128)
    description = models.CharField(blank=True, max_length=512)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


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

def imghelper(instance, filename):
    return instance.created.strftime('%Y/')+instance.created.strftime('%m%d/')+instance.created.strftime('%H%M')+'.jpg'

class PlantImg(models.Model):
    sensor = models.ForeignKey(Sensor, related_name="plantimg", on_delete=models.CASCADE)
    #sensor = models.ForeignKey("Plant", related_name="plantimg", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to=imghelper)

    def __str__(self):
        return str(self.id)
