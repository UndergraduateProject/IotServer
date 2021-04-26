from django.urls import path, include
from client import views
from knox import views as knox_views

urlpatterns = [
    path("register/", views.RegisterAPI.as_view()),
    path("login/", views.LoginAPI.as_view()),
    path("logout/",knox_views.LogoutView.as_view(), name='knox_logout'),
    path("user_testing/", views.UserAPI.as_view()), # for request.user testing
]
