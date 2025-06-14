from datetime import datetime

from rest_framework import serializers

from main.models import Data


class DataRequestSerializer(serializers.Serializer):
    param1 = serializers.CharField(required=False, default="-")
    param2 = serializers.CharField(required=False, default="-")
    param3 = serializers.CharField(required=False, default="-")
    param4 = serializers.CharField(required=False, default="-")
    device_id = serializers.IntegerField(required=True)


class GetDataRequestSerializer(serializers.Serializer):
    period = serializers.IntegerField(required=True)

    def validate_period(self, value):
        """Опционально: валидация периода"""
        if value < 0:
            raise serializers.ValidationError("Period cannot be in the future")
        return value


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
        extra_kwargs = {
            'timestamp': {'format': '%Y-%m-%d %H:%M:%S'},
        }
