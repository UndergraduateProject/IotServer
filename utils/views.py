from rest_framework.decorators import api_view
from utils.mail import sendmail
from utils.socket_connection import SocketMsg
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth import authenticate, login

@api_view(["GET", "POST"])
def certification(request):
    if request.method == "POST":
        sendmail(request.POST["mail"])
        return Response({"success": True})
    return Response({"success": False})

@api_view(["GET", "POST"])
def socket_connection(request):
    if request.method == "GET":
        print('123')
        socketmsg = SocketMsg("turn on led")
        socketmsg.send_to_iot()
        return Response({"success": True})
    return Response({"success": False})

@api_view(["GET", "POST"])
def login(request):
    #print (request.user)
    #return Response({"success" : False, "status" : "tesing"})
    username = request.data.get("username", None)
    password = request.data.get("password", None)
    if not username:
        return Response({"success" : False, "status" : "username is None"})
    elif not password:
        return Response({"success" : False, "status" : "password is None"})

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"success" : True , "status" : "logined"})
    return Response({"success" : False, "status" : "Please check your username and password"})

#utils endpoint
@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "mail_certification" : reverse("certification", request=request, format=format),
        "socket_connection" : reverse("socket_connection", request=request, format=format),
        "login" : reverse("login", request=request, format=format),
    })
