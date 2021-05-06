from django.urls import path, include
from rest_framework.authtoken import views
from user.views import RegisterAPI, UserAPI, logout

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/',  views.obtain_auth_token),
    path('logout/', logout),
    path('user/', UserAPI.as_view())
]
