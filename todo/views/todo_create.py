from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from common.mixins import APIViewResponseMixin

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


# Generic CreateAPIView class
class CreateTodoGenericAPIView(CreateAPIView, APIViewResponseMixin):
    serializer_class = TaskSerializerModel

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(
                data=request.data, context={"user": request.user}
            )
            # serializer.is_valid(raise_exception=True)
            if not serializer.is_valid():
                return self.failure_response(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    message=f"Xatolik: {serializer.errors}",
                )

            self.perform_create(serializer)

            return self.success_response(
                data=serializer.data,
                status_code=status.HTTP_201_CREATED,
                message="Todo created successfully",
            )
        except Exception as e:
            txt = {"error": str(e)}
            return self.error_response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message=txt,
            )


generic_create_todo_api_view = CreateTodoGenericAPIView.as_view()
