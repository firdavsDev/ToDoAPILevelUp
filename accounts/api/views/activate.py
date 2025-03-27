from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view

from accounts.email_verifycation import verify_email_code
from accounts.models import CustomUser


@api_view(["POST"])
def verify_email(request, email_code):
    try:
        user_id = verify_email_code(email_code)
        user = CustomUser.objects.get(id=user_id)
        user.is_active = True
        user.save()
        response_dict = {
            "message": "Email tasdiqlandi, iltimos login qiling",
        }
        return Response(response_dict, status=status.HTTP_200_OK)
    except Exception as e:
        response_dict = {
            "message": f"Xatolik yuz berdi: {e}"
        }
        return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)
