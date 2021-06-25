from rest_framework.decorators import api_view
from utils.mail import sendmail
from utils.water import action
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

@api_view(["GET"])
def water(request):
    if request.method == "GET":
        action()
        return Response({"success": True})
    return Response({"success": False})


@api_view(["GET", "POST"])
def certification(request):
    if request.method == "POST":
        password = sendmail(request.data["mail"])
        if password :
            return Response({
                "success": True,
                "verify": password,
                },status = status.HTTP_200_OK)
    return Response({"success": False},status=status.HTTP_500_INTERNAL_SERVER_ERROR
)

# utils endpoint


@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "mail_certification": reverse("certification", request=request, format=format),
        "action_water": reverse("water", request=request, format=format),
    })
