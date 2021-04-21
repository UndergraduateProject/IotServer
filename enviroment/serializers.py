from rest_framework import serializers
from enviroment.models import Sensor, Humid_Temp, Moisture


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['sensorID', 'sensorName']


class HumidityTemperatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Humid_Temp
        fields = ['id', 'created', 'humidity', 'temperature', 'heatIndex']


class MoistureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moisture
        fields = ['id', 'created', 'value']
