from rest_framework import serializers

from item.serializers import ItemSerializer
from . import models


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        # fields는 데이터베이스 속성을 제어합니다.
        fields =(
            'no',
            'mall_no',
            'name',
            'desc',
            'register_datetime',
            'update_information_datetime',
            'items',
        )
        model = models.Category


