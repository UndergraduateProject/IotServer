from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from client.models import Client
from client.serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
