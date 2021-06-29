from rest_framework.decorators import api_view
from utils.mail import sendmail
from utils.water import action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.views import APIView

class watering(APIView):
    def post(self, request, format=None):
        #這邊邏輯需要完善
        #volumn = request.data.get('volumn')
        #action不成功處理方法
        action()
        return Response({"INFO": "watering..."})

class MailCertificate(APIView):
    def post(self, request, format=None):
        mail = request.data.get('mail')
        if mail:
            password = sendmail(mail)
            return Response({"INFO":"success","verify": password}, status=status.HTTP_200_OK)
        return Response({"INFO":"no mail available"}, status=status.HTTP_400_BAD_REQUEST)


# utils endpoint
@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "watering": reverse("watering", request=request, format=format),
        "mail_certification": reverse("mail_certification", request=request, format=format),
    })
