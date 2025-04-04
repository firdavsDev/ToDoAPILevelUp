from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import RetrieveAPIView  # detail
from rest_framework.generics import UpdateAPIView  # update
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.mixins import ListModelMixin

from common.views import BaseAPIView
from todo.models import Task

from ..serializers.todo import TasksListSerializerModel


class ListTodoAPIView(BaseAPIView):
    # permission_classes = [AllowAny]
    # authentication_classes = []
    serializer_class = TasksListSerializerModel
    model = Task
    search_fields = ["title", "discription"]
    ordering_fields = ["title", "completed"]

    @swagger_auto_schema(
        operation_description="List all tasks",
        manual_parameters=[
            openapi.Parameter(
                "show_all",
                openapi.IN_QUERY,
                description="Show all tasks",
                type=openapi.TYPE_BOOLEAN,
            ),
            openapi.Parameter(
                "completed",
                openapi.IN_QUERY,
                description="Show completed tasks",
                type=openapi.TYPE_INTEGER,
            ),
        ],
    )
    def get(self, request):
        try:
            show_all = request.query_params.get("show_all", False)
            completed = request.query_params.get("completed", 0)
            if show_all:
                tasks = self.model.objects.filter(is_public=True)
            else:
                user = request.user
                tasks = self.model.objects.filter(user=user)

            if completed == "1":
                tasks = tasks.filter(completed=True)

            results = self.paginate_queryset(tasks, request, view=self)

            serializer = self.serializer_class(results, many=True)
            data = {
                "count": self.page.paginator.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "results": serializer.data,
            }
            return self.success_response(
                data=data,
                status_code=status.HTTP_200_OK,
                message="Tasks retrieved successfully",
            )

        except Exception as e:
            txt = {"error": str(e)}
            return self.error_response(
                data=txt,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message="Something went wrong",
            )


list_todo_api_view = ListTodoAPIView.as_view()

############################################################################################################


class ListTodoGenericAPIView(ListAPIView):
    # queryset = Task.objects.filter(user=request.user)
    serializer_class = TasksListSerializerModel
    search_fields = ["title", "discription"]
    ordering_fields = ["title", "completed"]

    def get_queryset(self):
        user = self.request.user
        tasks = Task.objects.filter(user=user)
        return tasks


list_todo_generic_api_view = ListTodoGenericAPIView.as_view()


################################################################################################################


# class ListTodoMixinAPIView(GenericAPIView, ListModelMixin):
#     serializer_class = TasksListSerializerModel

#     def get_queryset(self):
#         show_all = self.request.query_params.get("show_all", False)
#         completed = self.request.query_params.get("completed", 0)
#         user = self.request.user
#         tasks = Task.objects.filter(user=user)
#         return tasks

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# list_todo_mixin_api_view = ListTodoMixinAPIView.as_view()
