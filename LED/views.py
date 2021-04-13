from LED.models import LED
from django.contrib.auth.models import User
from LED.serializers import LEDSerializer,UserSerializer
from rest_framework import permissions
from LED.permissions import IsUsersOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import renderers

class LedViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `LEDusers` action.
    """
    queryset = LED.objects.all()
    serializer_class = LEDSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsUsersOrReadOnly]

    #這邊要注意default url path會是這個function的名字，若要自定義需使用"url_path"
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def LEDusers(self, request, *args, **kwargs):
        led = self.get_object()
        return Response(led.users)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer