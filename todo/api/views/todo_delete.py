from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ..serializers.todo import TaskSerializer

from todo.models import Task
from todo.permissions import IsTaskOwner
from rest_framework.generics import DestroyAPIView, GenericAPIView
from rest_framework.mixins import DestroyModelMixin


@permission_classes([IsTaskOwner])
@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_todo_detail(request, task_id):
    try:
        user = request.user
        task = Task.objects.get(id=task_id)
        if user == task.user:
            task.delete()
            return Response(
                {"success": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT
            )
        return Response(
                {"error": "This task is not yours"}, status=status.HTTP_204_NO_CONTENT
            )
    except Task.DoesNotExist:
        txt = {"error": "Task not found"}
        return Response(txt, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        txt = {"error": str(e)}
        return Response(txt, status=400)


class DeleteTodoAPIView(DestroyAPIView):
    serializer_class = TaskSerializer
    lookup_field = 'task_id'
    permission_classes = [IsTaskOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        task = Task.objects.filter(user=user)
        return task
    

delete_todo_api_view = DeleteTodoAPIView.as_view()


##########################################################################################

class DeleteTodoMixinAPIView(GenericAPIView,DestroyModelMixin):
    serializer_class=TaskSerializer
    permission_classes = [IsTaskOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        task = Task.objects.filter(user=user)
        return task
    
    def delete(self,request, *args , **kwargs):
        return self.destroy(request, *args, **kwargs)
    
delete_todo_mixin_api_view = DeleteTodoMixinAPIView.as_view()