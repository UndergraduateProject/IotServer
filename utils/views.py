from rest_framework.decorators import api_view
from utils.mail import sendmail
from utils.water import action
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET", "POST"])
def water(request):
    if request.method == "POST":
        action()
        return Response({"success": True})
    return Response({"success": False})


@api_view(["GET", "POST"])
def certification(request):
    if request.method == "POST":
        sendmail(request.POST["mail"])
        return Response({"success": True})
    return Response({"success": False})


# endpoint
@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "mail_certification": reverse(
                "certification", request=request, format=format
            ),
            "action_water": reverse("water", request=request, format=format),
        }
    )
