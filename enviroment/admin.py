from django.contrib import admin
from enviroment.models import Sensor, Humid_Temp, Moisture
# Register your models here.
admin.site.register(Sensor)
admin.site.register(Humid_Temp)
admin.site.register(Moisture)
