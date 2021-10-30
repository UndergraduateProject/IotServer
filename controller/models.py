from os import environ
from django.db import models
from django.contrib.auth.models import User

SWITCH_CHOICE = [
    ('ON', 'ON'),
    ('OFF', 'OFF')
]

CONDITION_TYPE_CHOICE = [
    ('watering', 'watering'),
    ('fan', 'fan'),
    ('light', 'light')
]

CONDITION_MODE_CHOICE = [
    ('default', 'default'),
    ('manual', 'manual')
]

CONDITION_OPERATOR_CHOICE = [
    ('<', '<'),
    ('>', '>')
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
    humidity = models.FloatField(default=-1)
    temperature = models.FloatField(default=-1)
    brightness = models.FloatField(default=-1)
    volume = models.FloatField(default=-1)
    mode = models.CharField(max_length=10, choices=CONDITION_MODE_CHOICE) # default or manual 
    type = models.CharField(max_length=10, choices=CONDITION_TYPE_CHOICE) # watering or fan
    status = models.CharField(max_length=3, choices=SWITCH_CHOICE, default='OFF') # on or off
    operator = models.CharField(max_length=1, choices=CONDITION_OPERATOR_CHOICE, default='<')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} -> {}".format(self.mode, self.type)


class WarningCondition(models.Model):
    user = models.ForeignKey('auth.User', related_name ='warning_condition', on_delete=models.PROTECT)
    moisture = models.FloatField(default=-1)
    humidity = models.FloatField(default=-1)
    temperature = models.FloatField(default=-1)
    brightness = models.FloatField(default=-1)
    volume = models.FloatField(default=-1)
    status = models.CharField(max_length=3, choices=SWITCH_CHOICE)
    operator = models.CharField(max_length=1, choices=CONDITION_OPERATOR_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class WarningRecord(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.timestamp)

class Plant(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    environment = models.CharField(max_length=300)
    livespan = models.FloatField()
    min_temp = models.FloatField(default=0)
    max_temp = models.FloatField(default=0)
    min_humidity = models.FloatField(default=0)
    max_humidity = models.FloatField(default=0)
    image = models.ImageField(null=True, blank=True)

class UsertoPlant(models.Model):
    user = models.ForeignKey('auth.User', related_name='User_plant', on_delete=models.PROTECT)
    plant = models.ForeignKey(Plant, related_name='User_plant', on_delete=models.PROTECT)

class Electricity(models.Model):
    quantity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Track(models.Model):
    position = models.FloatField()
    shift = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class WaterStorage(models.Model):
    volume = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)