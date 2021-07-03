from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from controller.models import Controller, Watering, LED, Fan, ActionCondition
from controller.serializers import (
    WateringSerializer,
    LEDSerializer,
    FanSerializer,
    ActionConditionSerializer,
)


class WateringViewSet(viewsets.ModelViewSet):
    queryset = Watering.objects.all()
    serializer_class = WateringSerializer
    filterset_fields = ["volume"]

    def perform_create(self, serializer):
        controller = self.request.data.get('controller') # get controller's name
        controller = get_object_or_404(Controller, name=controller)
        serializer.save(controller=controller)


class LEDViewSet(viewsets.ModelViewSet):
    queryset = LED.objects.all()
    serializer_class = LEDSerializer
    filterset_fields = ["red", "green", "blue", "brightness", "switch"]

    def perform_create(self, serializer):
        controller = self.request.data.get('controller') # get controller's name
        controller = get_object_or_404(Controller, name=controller)
        serializer.save(controller=controller)


class FanViewSet(viewsets.ModelViewSet):
    queryset = Fan.objects.all()
    serializer_class = FanSerializer

    def perform_create(self, serializer):
        controller = self.request.data.get('controller') # get controller's name
        controller = get_object_or_404(Controller, name=controller)
        serializer.save(controller=controller)

        
class ActionConditionViewSet(viewsets.ModelViewSet):
    queryset = ActionCondition.objects.all()
    serializer_class = ActionConditionSerializer
    filterset_fields = ["mode","type"]
    #lookup_field = "mode"
    #lookup_value_regex = "[^/]+"  

    def perform_create(self, serializer):
        controller = self.request.data.get('controller') # get controller's name
        controller = get_object_or_404(Controller, name=controller)
        serializer.save(controller=controller)
    
    # @action(detail=False, methods=['patch'])
    # def testing(self, request, pk=None):
    #     mode = request.data.get('mode')
    #     type = request.data.get('type')        
    #     action_condition = get_object_or_404(ActionCondition, mode=mode, type=type)
    #     serializer = self.get_serializer(action_condition)
    #     serializer.save
    #     print('tesing')
    #     return Response({'testing':serializer.data})