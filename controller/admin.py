from django.contrib import admin
from controller.models import Controller, Watering, LED, Fan, ActionCondition, Plant

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

admin.site.register(Controller, ControllerAdmin)
admin.site.register(Watering, WateringAdmin)
admin.site.register(LED, LEDAdmin)
admin.site.register(Fan, FanAdmin)
admin.site.register(ActionCondition, ActionConditionAdmin)
admin.site.register(Plant)
