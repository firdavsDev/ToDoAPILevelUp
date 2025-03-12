from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


def custom_disactie_action(modeladmin, request, queryset):
    queryset.update(is_active=False)


class CustomUserAdmin(UserAdmin):
    actions = [custom_disactie_action]
    list_display = (
        "email",
        "phone",
        "first_name",
        "is_staff",
        "is_active",
    )
    list_editable = (
        "is_staff",
        "is_active",
    )
    list_filter = (
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "phone",
                    "username",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "is_active",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ("email", "phone", "first_name")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
