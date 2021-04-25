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
from LED.views import LedViewSet, UserViewSet
from enviroment.views import SensorViewSet, HumidTempViewSet, MoistureViewSet
from client.views import ClientViewSet
from utils.views import certification

##authentications
from user.views import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views
from rest_framework.authtoken import views

router = DefaultRouter()
# LED urls
router.register(r"Led", LedViewSet)
router.register(r"users", UserViewSet)

# enviroment urls
router.register(r'sensor', SensorViewSet)
router.register(r'humidtemp', HumidTempViewSet)
router.register(r'moisture', MoistureViewSet)

# client urls
router.register(r"client", ClientViewSet)


# utilsrouter = DefaultRouter()
# utilsrouter.register(r"certification/", certification)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("utils/", include("utils.urls")),
    path("auth/", include("user.urls"))
    # path("auth/register/", RegisterAPI.as_view()),
    # path("auth/login/", LoginAPI.as_view()),
    # path("auth/logout/",knox_views.LogoutView.as_view(), name='knox_logout'),
    # path("auth/user_testing/", UserAPI.as_view()), # for request.user testing
    #path("api/auth/", include("knox.urls")),
]
