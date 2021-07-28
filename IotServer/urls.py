"""IotServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from enviroment.views import SensorViewSet, HumidTempViewSet, MoistureViewSet, PlantImgViewSet
from controller.views import WateringViewSet, LEDViewSet, FanViewSet, ActionConditionViewSet, PlantViewSet
from django.conf import settings
from django.conf.urls.static import static

## import API documentation
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()

# enviroment urls
router.register(r'Sensor', SensorViewSet)
router.register(r'Humidtemp', HumidTempViewSet)
router.register(r'Moisture', MoistureViewSet)
router.register(r'Plantimg', PlantImgViewSet)

# controller urls
router.register(r'Wartering', WateringViewSet)
router.register(r'LED', LEDViewSet)
router.register(r'Fan', FanViewSet)
router.register(r'ActionCondition', ActionConditionViewSet)
router.register(r'Plant', PlantViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="IOT server API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("utils/", include("utils.urls")),
    path("user/", include("user.urls")),
    ### API documentation
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# image storage
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)