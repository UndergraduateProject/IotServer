from rest_framework import serializers
from enviroment.models import Sensor, Humid_Temp, Moisture


class SensorSerializer(serializers.ModelSerializer):
    humid_temp = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="humid_temp-detail"
    )

    moisture = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="moisture-detail"
    )

    client = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="client-detail"
    )

    class Meta:
        model = Sensor
        fields = [
            "client",
            "client",
            "sensorID",
            "sensorName",
            "humid_temp",
            "moisture",
        ]


class HumidityTemperatureSerializer(serializers.ModelSerializer):

    sensor = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="sensor-detail"
    )

    class Meta:
        model = Humid_Temp
        fields = ["id", "created", "humidity", "temperature", "heatIndex", "sensor"]


class MoistureSerializer(serializers.ModelSerializer):

    sensor = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="sensor-detail"
    )

    class Meta:
        model = Moisture
        fields = ["id", "created", "value", "sensor", "sensor"]
