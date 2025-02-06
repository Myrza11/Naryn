from rest_framework import serializers
from sympy import false

from .models import *

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name", "price", "service_type", "user_id"]
        read_only_fields = ["user_id"]


class Service_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Type
        fields = '__all__'


class ServiceFilterSerializer(serializers.Serializer):
    minPrice = serializers.IntegerField(required=False, allow_null=True)
    maxPrice = serializers.IntegerField(required=False, allow_null=True)
    service_type = serializers.PrimaryKeyRelatedField(
        queryset=Service_Type.objects.all(), required=False, allow_null=True
    )

    def validate(self, attrs):
        min_price = attrs.get('minPrice', None)
        max_price = attrs.get('maxPrice', None)

        if min_price is not None and max_price is not None and max_price < min_price:
            raise ValidationError({"price": "Max price must be greater than min price"})

        return attrs


