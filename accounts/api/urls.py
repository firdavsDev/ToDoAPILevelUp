from django.urls import path

from .views import login_user, register_user, verify_email, logout

urlpatterns = [
    path("register/", register_user, name="register_user"),
    path("login/", login_user, name="login_user"),
    path("logout/", logout, name="logout"),
    path("verify-email/<str:email_code>/", verify_email, name="verify_email"),
]
