from django.contrib import admin
from enviroment.models import Sensor, HumidTemp, Moisture, PlantImg
# Register your models here.

class SensorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )


class HumidTempAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)


class MoistureAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)


class PlantImgAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)


admin.site.register(Sensor, SensorAdmin)
admin.site.register(HumidTemp, HumidTempAdmin)
admin.site.register(Moisture, MoistureAdmin)
admin.site.register(PlantImg, PlantImgAdmin)