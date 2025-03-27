from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.models import Task

from ..serializers.todo import TaskSerializerModel


@api_view(["PUT"])
def update_todo_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        todo_serializer_obj = TaskSerializerModel(instance=task, data=request.data)
        if todo_serializer_obj.is_valid():
            todo_serializer_obj.save()
            return Response(todo_serializer_obj.data, status=status.HTTP_200_OK)
        return Response(todo_serializer_obj.errors, status=400)
    except Task.DoesNotExist:
        txt = {"error": "Task not found"}
        return Response(txt, status=404)
    except Exception as e:
        txt = {"error": str(e)}
        return Response(txt, status=400)


@api_view(["PATCH"])
def partial_update_todo_detail(request, task_id):
    try:
        user = request.user
        task = Task.objects.get(id=task_id)
        todo_serializer_obj = TaskSerializerModel(
            instance=task, data=request.data, partial=True
        )
        if task.user == user and todo_serializer_obj.is_valid():
            todo_serializer_obj.save()
            data = {
                "message": "Task Updated Successfully",
                "data": todo_serializer_obj.data,
            }
            return Response(data, status=status.HTTP_200_OK)
        data = {
            "message": "Task not updated",
            "errors": todo_serializer_obj.errors,
        }
        return Response(data, status=400)
    except Task.DoesNotExist:
        txt = {"error": "Task not found"}
        return Response(txt, status=404)
    except Exception as e:
        raise e
