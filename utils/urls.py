from django.urls import path, include
from utils import views


urlpatterns = [
    path("mail_certification/", views.certification, name="certification"),
    path("socket_connection/", views.socket_connection, name="socket_connection"),
    path("", views.api_root),
]