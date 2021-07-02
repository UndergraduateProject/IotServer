from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from enviroment.models import Sensor, HumidTemp, Moisture, PlantImg
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
    queryset = HumidTemp.objects.all()
    serializer_class = HumidityTemperatureSerializer
    filterset_fields = ["humidity", "temperature", "heatIndex", "sensor__created"]

    def perform_create(self, serializer):
        sensor = self.request.data.get('sensor') # get sensor's name
        sensor = get_object_or_404(Sensor, name=sensor)
        serializer.save(sensor=sensor)


class MoistureViewSet(viewsets.ModelViewSet):
    queryset = Moisture.objects.all()
    serializer_class = MoistureSerializer
    filterset_fields = ["moisture"]

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