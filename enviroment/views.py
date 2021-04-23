from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters

from enviroment.models import Sensor, Humid_Temp, Moisture
from enviroment.serializers import (
    SensorSerializer,
    HumidityTemperatureSerializer,
    MoistureSerializer,
)


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filterset_fields = ["client__username"]


class HumidTempViewSet(viewsets.ModelViewSet):
    queryset = Humid_Temp.objects.all()
    serializer_class = HumidityTemperatureSerializer
    filterset_fields = ["humidity", "temperature", "heatIndex", "sensor__sensorID"]


class MoistureViewSet(viewsets.ModelViewSet):
    queryset = Moisture.objects.all()
    serializer_class = MoistureSerializer
    filterset_fields = ["value", "sensor__sensorID"]
