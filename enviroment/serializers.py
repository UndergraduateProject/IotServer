from rest_framework import serializers
from enviroment.models import Sensor, HumidTemp, Moisture, PlantImg
from django.contrib.auth.models import User


class SensorSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Sensor
        fields = ["name", "url", "description", "interval", "created", "owner"]

class HumidityTemperatureSerializer(serializers.ModelSerializer):

    sensor = serializers.HyperlinkedRelatedField(read_only=True, view_name="sensor-detail")

    class Meta:
        model = HumidTemp
        fields = ["id", "humidity", "temperature", "heatIndex", "timestamp", "sensor"]


class MoistureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moisture
        fields = ["id", "moisture", "timestamp"]
    

class PlantImgSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantImg
        fields = ["id", "image", "timestamp"]
