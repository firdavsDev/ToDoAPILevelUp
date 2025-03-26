from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import UserLoginSerializer, UserSerializer


class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(request_body=UserLoginSerializer)
    @transaction.atomic
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data["user"]
                response_serializer = UserSerializer(instance=user)
                # Create a token for the user
                refresh_obj = RefreshToken.for_user(user)
                response_dict = {
                    "message": "User registered successfully",
                    "data": serializer.data,
                    "refresh": str(refresh_obj),
                    "access": str(refresh_obj.access_token),
                }

                return Response(response_dict, status=status.HTTP_200_OK)
            response_dict = {
                "message": "User not logged in",
                "errors": serializer.errors,
            }
            return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_dict = {
                "message": "Error sodir bo'ldi",
                "errors": str(e),
            }
            return Response(response_dict, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Object yaratib keyin yaratilgan objectni url ga qo'shish
login_api_view = LoginAPIView.as_view()

# TODO write logout api function
