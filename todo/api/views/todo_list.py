from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from todo.models import Task

from ..serializers.todo import TasksListSerializerModel


class ListTodoAPIView(APIView, PageNumberPagination):
    # permission_classes = [AllowAny]
    # authentication_classes = []
    serializer_class = TasksListSerializerModel
    model = Task

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
            return self.get_paginated_response(serializer.data)

        except Exception as e:
            txt = {"error": str(e)}
            return Response(txt, status=400)


list_todo_api_view = ListTodoAPIView.as_view()

############################################################################################################


class ListTodoGenericAPIView(ListAPIView):
    # queryset = Task.objects.filter(user=request.user)
    serializer_class = TasksListSerializerModel

    def get_queryset(self):
        show_all = self.request.query_params.get("show_all", False)
        completed = self.request.query_params.get("completed", 0)
        user = self.request.user
        tasks = Task.objects.filter(user=user)
        return tasks


list_todo_generic_api_view = ListTodoGenericAPIView.as_view()
