from django.contrib import admin
from enviroment.models import Sensor, Humid_Temp, Moisture
# Register your models here.

class Humid_TempAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class MoistureAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Sensor)
admin.site.register(Humid_Temp,Humid_TempAdmin)
admin.site.register(Moisture,MoistureAdmin)