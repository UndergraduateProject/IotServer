from django.db import models

SWITCH_CHOICE = [
    ('ON', 'ON'),
    ('OFF', 'OFF')
]

CONDITION_TYPE_CHOICE = [
    ('watering', 'watering'),
    ('fan', 'fan')
]

CONDITION_MODE_CHOICE = [
    ('default', 'default'),
    ('manual', 'manual')
]

CONDITION_OPERATOR_CHOICE = [
    ('<', '<'),
    ('>', '<')
]

class Controller(models.Model):
    user = models.ForeignKey('auth.User', related_name ='controller', on_delete=models.PROTECT)
    name = models.CharField(primary_key=True, max_length=128)
    description = models.CharField(blank=True, max_length=512)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Watering(models.Model):
    controller = models.ForeignKey(Controller, related_name='watering', on_delete=models.PROTECT)
    volume = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.timestamp)


class LED(models.Model):
    controller = models.ForeignKey(Controller, related_name='LED', on_delete=models.PROTECT)
    red = models.FloatField()
    green = models.FloatField()
    blue = models.FloatField()
    brightness = models.FloatField()
    switch = models.CharField(max_length=3, choices=SWITCH_CHOICE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} -> {}'.format(str(self.timestamp),str(self.switch))


class Fan(models.Model):
    controller = models.ForeignKey(Controller, related_name='fan', on_delete=models.PROTECT)
    switch = models.CharField(max_length=3, choices=SWITCH_CHOICE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} -> {}'.format(str(self.timestamp),str(self.switch))


class ActionCondition(models.Model):
    controller = models.ForeignKey(Controller, related_name='action_condition', on_delete=models.PROTECT)
    moisture = models.FloatField(default=-1) 
    volume = models.FloatField(default=-1)
    temperature = models.FloatField(default=-1)
    mode = models.CharField(max_length=10, choices=CONDITION_MODE_CHOICE)
    type = models.CharField(max_length=10, choices=CONDITION_TYPE_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} -> {}".format(self.mode, self.type)

class WarningCondition(models.Model):
    user = models.ForeignKey('auth.User', related_name ='warning_condition', on_delete=models.PROTECT)
    moisture = models.FloatField()
    humidity = models.FloatField()
    temperature = models.FloatField()
    operator = models.CharField(max_length=1, choices=CONDITION_OPERATOR_CHOICE)
    status = models.CharField(max_length=3, choices=SWITCH_CHOICE)