from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from .mixins import APIViewResponseMixin


class BaseAPIView(APIView, APIViewResponseMixin, PageNumberPagination):
    """
    Create a base API view that combines APIView and APIViewResponseMixin
    Custom API View to handle all the common logic for all APIs
    """

    pass
