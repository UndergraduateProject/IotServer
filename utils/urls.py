from django.urls import path, include
from utils import views


urlpatterns = [
    path("mail_certification/", views.certification, name="certification"),
    path("", views.api_root),
]