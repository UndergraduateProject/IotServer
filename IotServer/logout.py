from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(["POST"])
def logout(request):
    request.user.auth_token.delete()
    return Response({'message':'logout success'}, status=status.HTTP_202_ACCEPTED)