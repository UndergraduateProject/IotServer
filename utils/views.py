from rest_framework.decorators import api_view
from utils.mail import sendmail
from utils.water import action
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth import authenticate, login

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
