from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .swagger_conf import schema_view
from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo/", include("todo.urls")),
    path("", home, name="home"),
    # API
    path("api/accounts/", include("accounts.urls")),
    path("api/todo/", include("todo.api.urls")),
    # JWT
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Swagger
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
]
