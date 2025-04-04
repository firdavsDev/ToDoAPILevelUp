from django.shortcuts import get_object_or_404

# imoort DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from todo.filters import TaskFilter
from todo.models import Task

from ..serializers.todo import TasksListSerializerModel


class TodoAPIView(ModelViewSet):
    """
    Todo API ViewSet
    Parameters:
        - is_done: bool
        - completed: bool
        - is_public: bool
    """

    # authentication_classes = []
    # permission_classes = []
    serializer_class = TasksListSerializerModel
    queryset = Task.objects.all()
    http_method_names = ["get", "post", "put", "patch"]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    # pagination_class = PageNumberPagination

    search_fields = ["title", "discription"]
    ordering_fields = ["title", "completed"]
    # filterset_fields = ["completed", "is_public", "user"]
    filterset_class = TaskFilter
    # ordering = ["-created_at"]
    # filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        return queryset

    # def list(self, request): #GET
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):  # GET
    #     user = self.request.user
    #     queryset = self.get_queryset()
    #     task = get_object_or_404(queryset, pk=pk)
    #     if task.user != user:
    #         return Response({"detail": "Not found."}, status=404)
    #     serializer = self.get_serializer(task)
    #     return Response(serializer.data)

    def create(self, request):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=201)

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
