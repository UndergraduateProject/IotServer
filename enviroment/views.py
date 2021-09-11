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
import pathlib
from leafmodel.leafillness import leaf_predict
from django.core.files.images import ImageFile
import socketio
import json

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

    '''
    1. 收到RAW image後先儲存
    2. call yolo model將產生的圖片更新到原本的model object裡
    3. 將yolo crops經過leaf illness model後儲存
    '''
    def perform_create(self, serializer):
        sensor = self.request.data.get('sensor') # get sensor's name
        sensor = get_object_or_404(Sensor, name=sensor)
        plantimage = serializer.save(sensor=sensor)

        # set up socket
        sio = socketio.Client()
        sio.connect('http://140.117.71.98:4001')
        # generate yolo image
        yolo_cmd = 'python detect.py --source ../media/{} --save-crop --weights best.pt'.format(plantimage.image)
        cur_path = pathlib.Path(__file__).parent.absolute() # get current path
        os.chdir(cur_path.parents[0] / 'yolo_v5')
        res = os.system(yolo_cmd) # excute yolo command
        plantimage_path = str(plantimage.image).split('/')[-1]  # get RAW plantimage file name
        yolo_image = open(f'runs/detect/exp/{plantimage_path}', 'rb') # read yolo image
        plantimage.yolo_image.save(plantimage_path, yolo_image) # save yolo image
        sio.emit('progress', {'raw_image':plantimage.image.url, 'yolo_image':plantimage.yolo_image.url})

        if res:
            return Response({'detail' : 'Error on yolo command'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) # erro happened
        
        # change path to gradcam
        os.chdir(cur_path.parents[0] / 'gradcam')
        # save crops
        crops_path = '../yolo_v5/runs/detect/exp/crops/leaf/'
        crops_num = len(os.listdir(crops_path))
        # create socket
        sio.emit('progress', {'total':crops_num})

        for i, crop_leaf_name in enumerate(os.listdir(crops_path)):
            crop_leaf_path = os.path.join(crops_path,crop_leaf_name)
            # leaf illness model 
            result = leaf_predict(crop_leaf_path) # leaf illness prediction
            gradcam_cmd = f'python main.py --image-path {crop_leaf_path} --network resnet50 --weight-path ../leafmodel/leafillness.pt'
            os.system(gradcam_cmd) # excute gradcam 
            cam_leaf_path = 'results/'+crop_leaf_name.split('.')[0]+'-resnet50-cam++.jpg'
            crop_img = PlantYoloCropImg.objects.create(plantimg=plantimage, image=ImageFile(open(crop_leaf_path, 'rb')), 
                                            gradcam_image=ImageFile(open(cam_leaf_path, 'rb')), prob=10) 
            sio.emit('progress', {'current':i+1, 'crop_image':crop_img.image.url, 'cam_image':crop_img.gradcam_image.url, 'prediction':json.dumps(result)})
            os.remove(crop_leaf_path)
            os.remove(cam_leaf_path)   
        sio.disconnect()  

class PlantYoloCropImgViewSet(viewsets.ModelViewSet):
    queryset = PlantYoloCropImg.objects.all()
    serializer_class = PlantYoloCropImgSerializer
    filterset_fields = ["plantimg__timestamp", 'prob']