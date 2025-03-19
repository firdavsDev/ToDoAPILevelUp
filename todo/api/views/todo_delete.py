from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from todo.models import Task
from todo.permissions import IsTaskOwner

from ..serializers.todo import TaskSerializer, TaskSerializerModel


@permission_classes([IsTaskOwner])
@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_todo_detail(request, task_id):
    try:
        # TODO is real user want to delete the task
        user = request.user
        task = Task.objects.get(id=task_id)

        task.delete()
        return Response(
            {"success": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
    except Task.DoesNotExist:
        txt = {"error": "Task not found"}
        return Response(txt, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        txt = {"error": str(e)}
        return Response(txt, status=400)
