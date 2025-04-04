from django.urls import path

from .views import login_api_view, logout_api_view, register_api_view, verify_email_api_view

urlpatterns = [
    path("register/", register_api_view, name="register_user"),
    path("login/", login_api_view, name="login_user"),
    path("logout/", logout_api_view, name="logout"),
    path("verify-email/<str:email_code>/", verify_email_api_view, name="verify_email"),
]
