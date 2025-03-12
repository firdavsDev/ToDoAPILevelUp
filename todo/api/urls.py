from django.urls import path

from .views import (
    create_todo_api_view,
    delete_todo_detail,
    get_todo_detail,
    list_todo_api_view,
    partial_update_todo_detail,
    update_todo_detail,
)

urlpatterns = [
    path("create/", create_todo_api_view, name="create_todo_api"),
    path("list/", list_todo_api_view, name="list_todo_api"),
    path("detail/<int:task_id>/", get_todo_detail, name="get_todo_detail"),
    path("update/<int:task_id>/", update_todo_detail, name="update_todo_detail"),
    path(
        "partial_update/<int:task_id>/",
        partial_update_todo_detail,
        name="partial_update_todo_detail",
    ),
    path("delete/<int:task_id>/", delete_todo_detail, name="delete_todo_detail"),
]
