from rest_framework.decorators import api_view
from utils.mail import sendmail
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

# @csrf_exempt
# def certification(request):
#     if request.method == "POST":
#         print(os.getcwd())
#         sendmail(request.POST["mail"])
#         return JsonResponse({'success':True}, safe=False)
#     return JsonResponse({'success':False}, safe=False)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET", "POST"])
def certification(request):
    if request.method == "POST":
        print(os.getcwd())
        sendmail(request.POST["mail"])
        return Response({"success": True})
    return Response({"success": False})


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "mail_certification": reverse(
                "certification", request=request, format=format
            ),
        }
    )
