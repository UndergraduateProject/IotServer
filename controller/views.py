from functools import partial
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
    
    @action(detail=False, methods=['put'])
    def updateCondition(self, request, pk=None):
        mode = request.data.get('mode')
        type = request.data.get('type')        
        action_condition = get_object_or_404(ActionCondition, mode=mode, type=type)
        if type == 'watering':
            action_condition.temperature = -1
        else:
            action_condition.moisture = -1
            action_condition.volume = -1
        serializer = self.get_serializer(action_condition, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'testing':serializer.data})
    
    def update(self, request, *args, **kwargs):
        mode = request.data.get('mode')
        type = request.data.get('type')
        instance = get_object_or_404(ActionCondition, mode=mode, type=type)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)