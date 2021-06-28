from rest_framework import serializers
from enviroment.models import Sensor, Humid_Temp, Moisture, PlantImg
from django.contrib.auth.models import User


class SensorSerializer(serializers.ModelSerializer):

    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Sensor
        fields = ["url", "name", "description", "created", "user_id", "username"]

class HumidityTemperatureSerializer(serializers.ModelSerializer):

    sensor = serializers.HyperlinkedRelatedField(read_only=True, view_name="sensor-detail")

    class Meta:
        model = Humid_Temp
        fields = ["id", "humidity", "temperature", "heatIndex", "created", "sensor"]


class MoistureSerializer(serializers.ModelSerializer):

    sensor = serializers.HyperlinkedRelatedField(read_only=True, view_name="sensor-detail")

    class Meta:
        model = Moisture
        fields = ["id", "value", "created", "sensor"]
    

class PlantImgSerializer(serializers.ModelSerializer):

    sensor = serializers.HyperlinkedRelatedField(read_only=True, view_name="sensor-detail")

    class Meta:
        model = PlantImg
        fields = ["id", "img", "created", "sensor"]
