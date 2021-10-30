from django.contrib import admin
from controller.models import (Controller, Watering, LED, Fan, 
                                ActionCondition, Plant, Electricity,
                                Track, WaterStorage, WarningCondition, 
                                UsertoPlant, WarningRecord)

# Register your models here.
class ControllerAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

class WateringAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp', )

class LEDAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp', )

class FanAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp', )

class ActionConditionAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at', )

class WarningConditionAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at', )

class ElectricityAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp', )

class TrackAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp', )

class WaterStorageAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp', )

class WarningRecordAdmim(admin.ModelAdmin):
    readonly_fields = ('timestamp', )

admin.site.register(Controller, ControllerAdmin)
admin.site.register(Watering, WateringAdmin)
admin.site.register(LED, LEDAdmin)
admin.site.register(Fan, FanAdmin)
admin.site.register(ActionCondition, ActionConditionAdmin)
admin.site.register(Plant)
admin.site.register(Electricity, ElectricityAdmin)
admin.site.register(Track)
admin.site.register(WaterStorage, WaterStorageAdmin)
admin.site.register(WarningCondition, WarningConditionAdmin)
admin.site.register(UsertoPlant)
admin.site.register(WarningRecord)
