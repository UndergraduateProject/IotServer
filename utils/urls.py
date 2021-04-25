from django.urls import path, include
from utils import views


urlpatterns = [
    path("mail_certification/", views.certification, name="certification"),
    path("action_water/", views.water, name="water"),
    path("login/", views.login, name="login"),
    path("", views.api_root),
]