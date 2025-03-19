from django.db import transaction
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.serializers import UserLoginSerializer, UserSerializer


# TODO Make AllowAny, And return refresh/access token
@transaction.atomic
@api_view(["POST"])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data["user"]
        response_serializer = UserSerializer(instance=user)
        # Create a token for the user
        token, created = Token.objects.get_or_create(user=user)
        response_dict = {
            "message": "User logged in successfully",
            "data": response_serializer.data,
        }
        response_dict["data"]["token"] = token.key
        return Response(response_dict, status=status.HTTP_200_OK)
    response_dict = {
        "message": "User not logged in",
        "errors": serializer.errors,
    }
    return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)


# TODO write logout api function
