from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from enviroment.models import Sensor, Humid_Temp, Moisture
from enviroment.serializers import SensorSerializer, HumidityTemperatureSerializer, MoistureSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class HumidTempViewSet(viewsets.ModelViewSet):
    queryset = Humid_Temp.objects.all()
    serializer_class = HumidityTemperatureSerializer


class MoistureViewSet(viewsets.ModelViewSet):
    queryset = Moisture.objects.all()
    serializer_class = MoistureSerializer
