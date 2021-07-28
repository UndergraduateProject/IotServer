from rest_framework import serializers
from controller.models import Watering, LED, Fan, ActionCondition, Plant
from django.contrib.auth.models import User

class WateringSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watering
        fields = ['id', 'volume', 'timestamp']


class LEDSerializer(serializers.ModelSerializer):

    class Meta:
        model = LED
        fields = ['id', 'red', 'green', 'blue', 'brightness', 'switch', 'timestamp']

    
class FanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fan
        fields = ['id', 'switch', 'timestamp']


class ActionConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActionCondition
        fields = ['id', 'moisture', 'volume', 'temperature', 'mode', 'type', 'created_at', 'update_at']

class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = ['id', 'name', 'description', 'environment', 'livespan']