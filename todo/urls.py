from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    create_todo_api_view,
    delete_todo_api_view,
    delete_todo_detail,
    delete_todo_mixin_api_view,
    generic_create_todo_api_view,
    get_todo_detail,
    get_todo_detail_api_view,
    list_todo_api_view,
    list_todo_generic_api_view,
    list_todo_mixin_api_view,
    partial_update_api_view,
    partial_update_todo_detail,
    update_todo_api_view,
    update_todo_detail,
)
from .views.todo_model_view import TodoAPIView

router = DefaultRouter()
router.register("viewsets", TodoAPIView)


urlpatterns = [
    # router.urls,
    path("", include(router.urls)),
    path("create/", create_todo_api_view, name="create_todo_api"),
    path(
        "generic_create/", generic_create_todo_api_view, name="generic_create_todo_api"
    ),
    path("list/", list_todo_api_view, name="list_todo_api"),
    path("list_generic/", list_todo_generic_api_view, name="list_todo_generic_api"),
    path("list_mixin/", list_todo_mixin_api_view, name="list_todo_mixin_api_view"),
    path("detail/<int:task_id>/", get_todo_detail, name="get_todo_detail"),
    path("update/<int:task_id>/", update_todo_api_view, name="update_todo_detail"),
    path(
        "partial_update/<int:task_id>/",
        partial_update_api_view,
        name="partial_update_todo_detail",
    ),
    path("delete/<int:task_id>/", delete_todo_api_view, name="delete_todo_detail"),
    path(
        "delete_mixin/<int:task_id>/",
        list_todo_mixin_api_view,
        name="list_todo_mixin_api_view",
    ),
]
