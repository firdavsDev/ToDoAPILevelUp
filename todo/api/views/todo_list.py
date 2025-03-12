from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from todo.models import Task

from ..serializers.todo import TaskSerializerModel


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_todo_api_view(request):
    try:

        tasks = Task.objects.filter(user=request.user)  # .first()

        # V1
        # tasks_json = []
        # for task in tasks:
        #     tasks_json.append(
        #         {
        #             "id": task.id,
        #             "title": task.title,
        #             "description": task.discription,
        #             "completed": task.completed,
        #         }
        #     )
        # tasks_json = json.dumps(tasks_json)

        # v2
        # todo_serializer_obj = TaskSerializer(
        #     tasks
        # )  # many=True when tasks is a queryset of multiple objects
        # tasks_json = todo_serializer_obj.data  # converts to json data

        # v3
        todo_serializer_obj = TaskSerializerModel(
            tasks, many=True
        )  # many=True when tasks is a queryset of multiple objects
        tasks_json = todo_serializer_obj.data  # converts to json data

        return Response(tasks_json, status=status.HTTP_200_OK)
    except Exception as e:
        txt = {"error": str(e)}
        return Response(txt, status=400)


# import requests

# url = "http://127.0.0.1:8000/todo/api/list/"
# headers = {"Authorization": "Token 5b5844d46d40ec4a694d3bfdc4e2062541456583"}
# response = requests.get(url, headers=headers)
# print(response.json())
