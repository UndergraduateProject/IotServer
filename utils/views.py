from rest_framework.decorators import api_view
from utils.mail import sendmail
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def certification(request):
    if request.method == "POST":
        print(os.getcwd())
        sendmail(request.POST["mail"])
        return JsonResponse({'success':True}, safe=False)
    return JsonResponse({'success':False}, safe=False)