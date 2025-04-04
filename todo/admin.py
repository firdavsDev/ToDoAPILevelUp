from django.contrib import admin

from .models import Task


def make_public(modeladmin, request, queryset):
    queryset.update(is_public=True)


class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "is_public"]
    list_filter = ["completed"]
    search_fields = ["user__username", "title"]
    list_per_page = 20
    actions_on_top = True
    actions = [make_public]


admin.site.register(Task, TaskAdmin)
