from rest_framework import serializers
from enviroment.models import Sensor, Humid_Temp, Moisture


class SensorSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    clientID = serializers.HyperlinkedRelatedField(
        read_only= True,
        view_name='client-detail')
    client_id = serializers.ReadOnlyField(source='clientID.username')
    class Meta:
        model = Sensor
        fields = ['url', 'sensorID', 'sensorName', 'clientID', 'client_id']
=======
    humid_temp = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="humid_temp-detail"
    )

    moisture = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="moisture-detail"
    )

    client = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="client-detail"
    )

    class Meta:
        model = Sensor
        fields = ['client', 'client', 'sensorID',
                  'sensorName', 'humid_temp', 'moisture']
>>>>>>> a95922caf693df3b893fe09f64e6753bfd77a21c


class HumidityTemperatureSerializer(serializers.ModelSerializer):

    sensor = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="sensor-detail"
    )

    class Meta:
        model = Humid_Temp
        fields = ['id', 'created', 'humidity',
                  'temperature', 'heatIndex', 'sensor']


class MoistureSerializer(serializers.ModelSerializer):

    sensor = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="sensor-detail"
    )

    class Meta:
        model = Moisture
        fields = ['id', 'created', 'value', 'sensorID', 'sensor']
