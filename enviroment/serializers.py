from rest_framework import serializers
from enviroment.models import Sensor, Humid_Temp, Moisture


class SensorSerializer(serializers.ModelSerializer):
    clientID = serializers.HyperlinkedRelatedField(
        read_only= True,
        view_name='client-detail')
    client_id = serializers.ReadOnlyField(source='clientID.username')
    class Meta:
        model = Sensor
        fields = ['url', 'sensorID', 'sensorName', 'clientID', 'client_id']


class HumidityTemperatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Humid_Temp
        fields = ['id', 'created', 'humidity', 'temperature', 'heatIndex']


class MoistureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moisture
        fields = ['id', 'created', 'value']
