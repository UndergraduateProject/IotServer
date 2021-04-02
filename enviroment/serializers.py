from rest_framework import serializers
from enviroment.models import Humidity, Temperature


class HumiditySerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Humidity
        fields = ['id', 'created', 'value']


class TemperatureSerializer(serializers.ModelSerializer):

    created = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Temperature
        fields = ['id', 'created', 'value']
