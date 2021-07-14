from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from enviroment.models import Sensor, HumidTemp, Moisture, PlantImg, PlantYoloCropImg
from enviroment.serializers import (
    SensorSerializer,
    HumidityTemperatureSerializer,
    MoistureSerializer,
    PlantImgSerializer,
    PlantYoloCropImgSerializer,
)

import os
from django.core.files import File 

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
        plantimage = serializer.save(sensor=sensor)

        yolo_cmd = 'python detect.py --source ../media/{} --weights best.pt'.format(plantimage.image) # append full path
        os.chdir('yolov5')
        res = os.system(yolo_cmd) # if success, get 0
        plantimage_path = str(plantimage.image).split('/')[-1]  # get plantimage file name
        yolo_image = open(f'runs/detect/exp/{plantimage_path}', 'rb') # yolo result
        plantimage.yolo_image.save(plantimage_path, yolo_image) # update yolo image
        if res:
            return Response({'detail' : 'Erro on yolo command'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) # erro happened
        

class HumidTempViewSet(viewsets.ModelViewSet):
    queryset = PlantYoloCropImg.objects.all()
    serializer_class = PlantYoloCropImgSerializer
    filterset_fields = ["plantimg__timestamp", 'prob']

    def perform_create(self, serializer):
        img_id = self.request.data.get('plantimg') # get sensor's name
        plantimg = get_object_or_404(PlantImg, id=img_id)
        serializer.save(plantimg=plantimg)
