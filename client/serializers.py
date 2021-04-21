from rest_framework import serializers
from client.models import Client


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
