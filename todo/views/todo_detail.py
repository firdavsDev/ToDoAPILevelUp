from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from todo.models import Task

from ..serializers.todo import TaskSerializerModel


@api_view(["GET"])
def get_todo_detail(request, task_id):
    try:
        user = request.user
        task = Task.objects.get(id=task_id)
        if task.user != user:
            txt = {"error": "Task not found"}
            return Response(txt, status=status.HTTP_404_NOT_FOUND)
        todo_serializer_obj = TaskSerializerModel(instance=task)
        return Response(todo_serializer_obj.data, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        txt = {"error": "Task not found"}
        return Response(txt, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        txt = {"error": str(e)}
        return Response(txt, status=400)


class GetTodoDetailAPIView(RetrieveAPIView):
    serializer_class = TaskSerializerModel
    lookup_field = 'task_id'

    def get_queryset(self):
        user = self.request.user
        task = Task.objects.filter(user=user)
        return task
    

get_todo_detail_api_view = GetTodoDetailAPIView.as_view()