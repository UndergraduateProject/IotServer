from rest_framework import serializers
from client.models import Client
from enviroment.models import Sensor


<<<<<<< HEAD
class ClientSerializer(serializers.ModelSerializer):
    sensors = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name= "sensor-detail")
    class Meta:
        model = Client
        fields = ["id", "username", "password", "email", "verify", "enable", "sensors"]
=======
class ClientSerializer(serializers.HyperlinkedModelSerializer):

    sensors = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name="sensor-detail"
    )

    class Meta:
        model = Client
        fields = ["id", "username", "password",
                  "email", "verify", "enable", "sensors"]
>>>>>>> a95922caf693df3b893fe09f64e6753bfd77a21c
