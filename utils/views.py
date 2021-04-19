from rest_framework.decorators import api_view
from utils.mail import sendmail
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.reverse import reverse


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
        }
    )
