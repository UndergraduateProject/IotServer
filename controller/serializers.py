from rest_framework import serializers
from controller.models import Watering, LED, Fan, ActionCondition, Plant, Electricity, Track, WaterStorage, WarningCondition
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
        fields = '__all__'


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = ['id', 'name', 'description', 'environment', 'livespan']

class WarningConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = WarningCondition
        fields = '__all__'

class ElectricitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Electricity
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = '__all__'


class WaterStorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = WaterStorage
        fields = '__all__'