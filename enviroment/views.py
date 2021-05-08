from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import permissions

from enviroment.models import Sensor, Humid_Temp, Moisture
from enviroment.serializers import (
    SensorSerializer,
    HumidityTemperatureSerializer,
    MoistureSerializer,
)


class SensorViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filterset_fields = ["user__username"]


class HumidTempViewSet(viewsets.ModelViewSet):
    queryset = Humid_Temp.objects.all()
    serializer_class = HumidityTemperatureSerializer
    filterset_fields = ["humidity", "temperature", "heatIndex", "sensor__sensorName"]


class MoistureViewSet(viewsets.ModelViewSet):
    queryset = Moisture.objects.all()
    serializer_class = MoistureSerializer
    filterset_fields = ["value", "sensor__sensorName"]
