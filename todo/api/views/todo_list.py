from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.models import Task

from ..serializers.todo import TasksListSerializerModel


@api_view(["GET"])
def list_todo_api_view(request):
    try:
        show_all = request.query_params.get("show_all", False)
        completed = request.query_params.get("completed", 0)
        if show_all:
            tasks = Task.objects.filter(is_public=True)
        else:
            user = request.user
            tasks = Task.objects.filter(user=user)

        if completed == "1":
            tasks = tasks.filter(completed=True)

        # -----------------------------------------------------------
        page_number = request.query_params.get("page_number", 1)
        page_size = request.query_params.get("page_size", 2)

        paginator = Paginator(tasks, page_size)
        page = paginator.page(page_number)
        page_count = paginator.num_pages
        total_count = paginator.count
        serializer = TasksListSerializerModel(page, many=True)
        # -----------------------------------------------------------
        response = {
            "total_count": total_count,
            "page_count": page_count,
            "page_number": page_number,
            "page_size": page_size,
            "data": serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        txt = {"error": str(e)}
        return Response(txt, status=400)


# import requests

# Token Authentication
# url = "http://127.0.0.1:8000/todo/api/list/"
# headers = {"Authorization": "Token 5b5844d46d40ec4a694d3bfdc4e2062541456583"}
# response = requests.get(url, headers=headers)
# print(response.json())

# # Basic Authentication
# url = "http://"

# response = requests.get(url, auth=("admin", "admin"))
# print(response.json())

# # Session Authentication
# url = "http://"
# response = requests.get(url, cookies={"sessionid": "1"})
# print(response.json())
