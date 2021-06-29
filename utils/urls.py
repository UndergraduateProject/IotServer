from django.urls import path, include
from utils.views import watering, MailCertificate, api_root


urlpatterns = [
    path("watering/", watering.as_view(), name="watering"),
    path("mail_certification/", MailCertificate.as_view(), name='mail_certification'),
    path("", api_root),
]