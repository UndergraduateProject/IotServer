from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import viewsets, generics, permissions

from .serializers import UserSerializer, RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework import status

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data
        })

class UserAPI(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

@api_view(["POST"])
def logout(request):
    request.user.auth_token.delete()
    return Response({'message':'logout success'}, status=status.HTTP_202_ACCEPTED)