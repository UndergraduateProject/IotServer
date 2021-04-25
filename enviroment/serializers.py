from rest_framework import serializers
from enviroment.models import Sensor, Humid_Temp, Moisture


class SensorSerializer(serializers.ModelSerializer):

    client = serializers.HyperlinkedRelatedField(
        read_only= True,
        view_name='client-detail')
    client_name = serializers.ReadOnlyField(source='client.username')
    class Meta:
        model = Sensor
        fields = ['url', 'sensorID', 'sensorName', 'client', 'client_name']

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
        fields = ["id", "created", "value", "sensor"]
