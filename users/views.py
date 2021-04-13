from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from users.models import User
from users.serializers import UsersSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer