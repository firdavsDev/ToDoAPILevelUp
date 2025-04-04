from rest_framework import status
from rest_framework.response import Response


class APIViewResponseMixin:
    """
    Mixin to customize the response format
    """

    SUCCESS = "success"  # 200
    FAILURE = "failure"  # 400
    ERROR = "error"  # 500

    @classmethod
    def success_response(cls, data=None, message=None, status_code=status.HTTP_200_OK):
        """
        Returns Success Response
        """
        response_data = {"status_code": status_code, "status": cls.SUCCESS}
        if message is not None:
            response_data["message"] = message
        if data is not None:
            response_data["data"] = data
        return Response(response_data, status=status_code)

    @classmethod
    def failure_response(
        cls, data=None, message=None, status_code=status.HTTP_400_BAD_REQUEST
    ):
        """
        Returns Failure Response
        """
        response_data = {"status_code": status_code, "status": cls.FAILURE}
        if message is not None:
            response_data["message"] = message
        if data is not None:
            response_data["data"] = data
        return Response(response_data, status=status_code)

    @classmethod
    def error_response(
        cls, data=None, message=None, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    ):
        """
        Returns Error Response
        """
        response_data = {"status_code": status_code, "status": cls.ERROR}
        if message is not None:
            response_data["message"] = message
        if data is not None:
            response_data["data"] = data
        return Response(response_data, status=status_code)
