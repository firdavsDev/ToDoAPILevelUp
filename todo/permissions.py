from rest_framework.permissions import SAFE_METHODS, BasePermission

from todo.models import Task


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsTaskOwner(BasePermission):
    def has_permission(self, request, view):
        task_id = view.kwargs.get("task_id")
        if task_id:
            task = Task.objects.filter(id=task_id, user=request.user).exists()
            return task  # Returns True if the user owns the task, False otherwise
        return False
