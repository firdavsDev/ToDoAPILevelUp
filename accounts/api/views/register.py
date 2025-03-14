from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.serializers import UserSerializer


@transaction.atomic
@api_view(["POST"])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response_dict = {
            "message": "User registered successfully",
            "data": serializer.data,
        }
        return Response(response_dict, status=status.HTTP_201_CREATED)
    response_dict = {
        "message": "User not registered",
        "errors": serializer.errors,
    }
    return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)
