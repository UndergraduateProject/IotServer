from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from LED.models import LED
from LED.serializers import LEDSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from LED.permissions import IsUsersOrReadOnly

class LEDList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = LED.objects.all()
    serializer_class = LEDSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(users=self.request.user)

class LEDDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a LED instance.
    """
    queryset = LED.objects.all()
    serializer_class = LEDSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsUsersOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'LED': reverse('LED-list', request=request, format=format)
    })

class LEDUsers(generics.GenericAPIView):
    queryset = LED.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)