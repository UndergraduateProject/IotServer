# currently not working

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from enviroment import views

router = DefaultRouter()
router.register(r'/sensor', views.SensorViewSet)
router.register(r'/humidtemp', views.HumidTempViewSet)
router.register(r'/moisture', views.MoistureViewSet)
router.register(r'plantimg', views.PlantImgViewSet)

urlpatterns = [
    path('', include(router.urls))
]
