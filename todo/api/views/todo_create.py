from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.todo import TaskSerializerModel


# CBV APIView class
class CreateTodoAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializerModel

    @swagger_auto_schema(
        request_body=TaskSerializerModel,
        responses={
            201: openapi.Response(
                description="Todo created successfully",
                examples={
                    "application/json": {
                        "message": "Todo created successfully",
                        "data": {},
                    }
                },
            ),
            400: openapi.Response(
                description="Todo not created",
                examples={
                    "application/json": {
                        "message": "Todo not created",
                        "errors": {
                            "task": ["This field is required."],
                            "description": ["This field is required."],
                        },
                    }
                },
            ),
        },
    )
    def post(self, request):
        try:
            user = request.user
            todo_serializer_obj = self.serializer_class(
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


create_todo_api_view = CreateTodoAPIView.as_view()
