from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response
from core.models import Example
from . import serializers


class ExampleView(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_id="example",
        operation_description="Example Endpoint SBTUR",
        # request_body=serializers.ExampleSerializer,
        responses={200: '{"text": "Example Text"}'},
    )
    def list(self, request):
        example = Example(text="Example Endpoint SBTUR")
        serializer = serializers.ExampleSerializer(example)

        return Response(
            {"text": serializer.data.get("text")}, status=status.HTTP_200_OK
        )
