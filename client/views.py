from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import viewsets, permissions

from client.models import Client
from client.serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permissions_classes = [permissions.IsAuthenticated]
    filterset_fields = ["username", "email"]

    def get_queryset(self):
        return self.request.user.clients.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)