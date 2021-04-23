from rest_framework import serializers
from client.models import Client
from enviroment.models import Sensor

class ClientSerializer(serializers.ModelSerializer):
    sensors = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name= "sensor-detail")
    class Meta:
        model = Client
        fields = ["id", "username", "password", "email", "verify", "sensors"]