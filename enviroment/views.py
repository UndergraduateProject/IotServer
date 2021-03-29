from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from enviroment.models import Humidity,Temperature
from enviroment.serializers import HumiditySerializer,TemperatureSerializer



class HumidityViewSet(viewsets.ModelViewSet):
    queryset = Humidity.objects.all()
    serializer_class = HumiditySerializer


class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
