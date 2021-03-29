from django.contrib.auth.models import User, Group
from rest_framework import serializers
from LED.models import LED


class LEDSerializer(serializers.ModelSerializer):
    #user = serializers.ReadOnlyField(source='users.username')

    class Meta:
        model = LED
        fields = ['id','name','gpio_num','color','status','onoff','authenti_testing']


class UserSerializer(serializers.ModelSerializer):
    #LEDs = serializers.HyperlinkedRelatedField(many=True, view_name='LED-list', read_only=True)
    LEDs = serializers.PrimaryKeyRelatedField(many=True, queryset=LED.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'LEDs']
