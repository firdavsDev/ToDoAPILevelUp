from django.contrib import messages
from django.shortcuts import redirect

from accounts.email_verifycation import verify_email_code
from accounts.models import CustomUser

# TODO remove any redirects intead return response and use api


def verify_email(request, email_code):
    try:
        user_id = verify_email_code(email_code)
        user = CustomUser.objects.get(id=user_id)
        user.is_active = True
        user.save()
        messages.success(request, "Email tasdiqlandi, iltimos login qiling")
        return redirect("login_user")
    except Exception as e:
        messages.error(request, f"Xatolik yuz berdi: {e}")
        return redirect("register_user")
