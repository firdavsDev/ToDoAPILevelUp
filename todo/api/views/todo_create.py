from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..serializers.todo import TaskSerializerModel


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_todo_api_view(request):
    try:
        user = request.user
        todo_serializer_obj = TaskSerializerModel(
            data=request.data, context={"user": user}
        )
        if todo_serializer_obj.is_valid():
            todo_serializer_obj.save()
            data = todo_serializer_obj.data
            response_dict = {
                "message": "Todo created successfully",
                "data": data,
            }
            return Response(response_dict, status=status.HTTP_201_CREATED)
        response_dict = {
            "message": "Todo not created",
            "errors": todo_serializer_obj.errors,
        }
        return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        txt = {"error": str(e)}
        return Response(txt, status=400)
