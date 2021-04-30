from rest_framework import serializers
from user.models import Client
from enviroment.models import Sensor
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate

class ClientSerializer(serializers.ModelSerializer):
    sensors = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name= "sensor-detail")
    class Meta:
        model = Client
        fields = ["id", "username", "password", "email", "verify", "sensors"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password' : {'write_only' : True}}
    def create(self, validated_data):
        user = User.objects.create_user(validated_data["username"], validated_data['email'], validated_data['password']) 
        return user