import logging
from datetime import datetime, timedelta

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from api.v1.serializers.serializers import (
    DataRequestSerializer,
    GetDataRequestSerializer, DataSerializer,
)
from main.models import Data


log = logging.getLogger(__name__)


class DeviceViewSet(viewsets.GenericViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = []

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='period',
                type=int,
                location=OpenApiParameter.QUERY,
                description='Период в минутах',
                required=True
            )
        ]
    )
    @action(
        methods=["GET"],
        detail=False,
    )
    def get_data_by_period(self, request):
        """
        Возвращает данные за указанный период
        """
        serializer = GetDataRequestSerializer(data=request.query_params)
        if serializer.is_valid():
            period = int(serializer.validated_data['period'])
            if period == 0:
                data = Data.objects.order_by("-timestamp")[:200]
            else:
                data = Data.objects.filter(
                    timestamp__gte=datetime.now() - timedelta(minutes=period)
                ).order_by("-timestamp")
            data_serializer = DataSerializer(data, many=True)
            return Response(
                {
                    "data": data_serializer.data
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(
        methods=["POST"],
        detail=False,
        serializer_class=DataRequestSerializer,
    )
    def save_data_from_device(self, request):
        """
        Заносит данные о показаниях датчика в базу данных
        """
        serializer = DataRequestSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        Data.objects.create(**serializer.validated_data)
        log.info(serializer.validated_data)
        return Response(
            {
                "status": "ok"
            },
            status=status.HTTP_200_OK,
        )
