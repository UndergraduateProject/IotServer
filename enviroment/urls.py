from django.urls import path,include
from rest_framework.routers import DefaultRouter
from enviroment import views

router = DefaultRouter()
router.register(r'humidity', views.HumidityViewSet)
router.register(r'temperature', views.TemperatureViewSet)

urlpatterns = [
    path('enviroment/',include(router.urls))
]