from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from accounts.serializers import UserSerializer


@transaction.atomic
@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # manually generate refresh token
            refresh_obj = RefreshToken.for_user(user)
            response_dict = {
                "message": "User registered successfully",
                "data": serializer.data,
                "refresh": str(refresh_obj),
                "access": str(refresh_obj.access_token),
            }
            return Response(response_dict, status=status.HTTP_201_CREATED)
        response_dict = {
            "message": "User not registered",
            "errors": serializer.errors,
        }
        return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        response_dict = {"message": str(e)}
        return Response(response_dict, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    @transaction.atomic
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                # manually generate refresh token
                refresh_obj = RefreshToken.for_user(user)
                response_dict = {
                    "message": "User registered successfully",
                    "data": serializer.data,
                    "refresh": str(refresh_obj),
                    "access": str(refresh_obj.access_token),
                }
                return Response(response_dict, status=status.HTTP_201_CREATED)
            response_dict = {
                "message": "User not registered",
                "errors": serializer.errors,
            }
            return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_dict = {"message": str(e)}
            return Response(response_dict, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        
        

register_api_view = RegisterAPIView.as_view()