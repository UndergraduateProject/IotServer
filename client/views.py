from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import viewsets, generics, permissions

from client.models import Client
from client.serializers import ClientSerializer

from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permissions_classes = [permissions.IsAuthenticated]
    filterset_fields = ["username", "email"]

    def get_queryset(self):
        return self.request.user.clients.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


#auth API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #print(request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : AuthToken.objects.create(user)[1]
        })
 
class UserAPI(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user