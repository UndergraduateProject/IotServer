from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import filters
from django.shortcuts import get_object_or_404

from enviroment.models import Sensor, Humid_Temp, Moisture, PlantImg
from enviroment.serializers import (
    SensorSerializer,
    HumidityTemperatureSerializer,
    MoistureSerializer,
    PlantImgSerializer,
)


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filterset_fields = ["user__username"]


class HumidTempViewSet(viewsets.ModelViewSet):
    queryset = Humid_Temp.objects.all()
    serializer_class = HumidityTemperatureSerializer
    filterset_fields = ["humidity", "temperature", "heatIndex", "sensor__created"]

    def perform_create(self, serializer):
        sensor = self.request.data.get('sensor') # get sensor's name
        sensor = get_object_or_404(Sensor, name=sensor)
        serializer.save(sensor=sensor)


class MoistureViewSet(viewsets.ModelViewSet):
    queryset = Moisture.objects.all()
    serializer_class = MoistureSerializer
    filterset_fields = ["value", "sensor"]

    def perform_create(self, serializer):
        sensor = self.request.data.get('sensor') # get sensor's name
        sensor = get_object_or_404(Sensor, name=sensor)
        serializer.save(sensor=sensor)

        

class PlantImgViewSet(viewsets.ModelViewSet):
    queryset = PlantImg.objects.all()
    serializer_class = PlantImgSerializer

    def perform_create(self, serializer):
        sensor = self.request.data.get('sensor') # get sensor's name
        sensor = get_object_or_404(Sensor, name=sensor)
        serializer.save(sensor=sensor)