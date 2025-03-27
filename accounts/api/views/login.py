from django.db import transaction
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login as logout

from accounts.serializers import UserLoginSerializer, UserSerializer


@transaction.atomic
@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data["user"]
        response_serializer = UserSerializer(instance=user)
        # Create a token for the user
        token, created = Token.objects.get_or_create(user=user)
        refresh_obj = RefreshToken.for_user(user)
        response_dict = {
            "message": "User logged in successfully",
            "data": response_serializer.data,
            "refresh": str(refresh_obj),
            "access": str(refresh_obj.access_token),
        }
        response_dict["data"]["token"] = token.key
        return Response(response_dict, status=status.HTTP_200_OK)
    response_dict = {
        "message": "User not logged in",
        "errors": serializer.errors,
    }
    return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def logout_user(request):
    logout(request)
    response_dict = {
        "message": "User Logout successfuly",
    }
    return Response(response_dict, status=status.HTTP_200_OK)