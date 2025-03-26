from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from todo.models import Task

from ..serializers.todo import TasksListSerializerModel


class TodoAPIView(ModelViewSet):
    serializer_class = TasksListSerializerModel
    queryset = Task.objects.all()
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    # pagination_class = PageNumberPagination

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["completed", "is_public"]
    # search_fields = ["task", "description"]
    # ordering_fields = ["task", "created_at"]
    # ordering = ["-created_at"]

    # def list(self, request):
    #    pass

    # def create(self, request):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
