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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from enviroment.views import SensorViewSet, HumidTempViewSet, MoistureViewSet, PlantImgViewSet
from controller.views import WateringViewSet, LEDViewSet, FanViewSet, ActionConditionViewSet
from django.conf import settings
from django.conf.urls.static import static


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


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("utils/", include("utils.urls")),
    path("user/", include("user.urls"))
]

# image storage
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)