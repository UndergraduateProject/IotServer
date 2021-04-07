from django.urls import path,include
from rest_framework.routers import DefaultRouter
from LED import views

router = DefaultRouter()
router.register(r'Led', views.LedViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]