from rest_framework import serializers
from enviroment.models import Sensor, Humid_Temp, Moisture, PlantImg
from django.contrib.auth.models import User


class SensorSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Sensor
        fields = ["id", "url", "sensorName",  "owner"]

class HumidityTemperatureSerializer(serializers.ModelSerializer):

    sensor = serializers.HyperlinkedRelatedField(read_only=True, view_name="sensor-detail")

    class Meta:
        model = Humid_Temp
        fields = ["id", "created", "humidity", "temperature", "heatIndex", "sensor"]


class MoistureSerializer(serializers.ModelSerializer):

    sensor = serializers.HyperlinkedRelatedField(read_only=True, view_name="sensor-detail")

    class Meta:
        model = Moisture
        fields = ["id", "created", "value", "sensor"]
    

class PlantImgSerializer(serializers.ModelSerializer):

    sensor = serializers.HyperlinkedRelatedField(read_only=True, view_name="sensor-detail")

    class Meta:
        model = PlantImg
        fields = ["id", "created", "sensor", "img"]
