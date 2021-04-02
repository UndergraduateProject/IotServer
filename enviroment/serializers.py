from rest_framework import serializers
from enviroment.models import Humidity, Temperature


class HumiditySerializer(serializers.ModelSerializer):

    class Meta:
        model = Humidity
        fields = ['id', 'created', 'value','sensorId']


class TemperatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Temperature
        fields = ['id', 'created', 'value','sensorId']
