from django.contrib.auth.models import User, Group
from rest_framework import serializers
from LED.models import LED


class LEDSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.ReadOnlyField(source='users.username')

    class Meta:
        model = LED
        fields = ['id','name','gpio_num','color','status','onoff','authenti_testing','users']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    LEDs = serializers.HyperlinkedRelatedField(many=True, view_name='LED-detail', read_only=True)
    #LEDs = serializers.PrimaryKeyRelatedField(many=True, queryset=LED.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'LEDs']
