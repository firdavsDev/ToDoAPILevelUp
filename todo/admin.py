from django.contrib import admin

from .models import Task


def make_public(modeladmin, request, queryset):
    queryset.update(is_public=True)


class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "is_public"]
    list_filter = ["completed"]
    search_fields = ["user"]
    actions = [make_public]


admin.site.register(Task, TaskAdmin)
