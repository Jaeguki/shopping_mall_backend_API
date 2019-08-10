from rest_framework import serializers

from category.serializers import CategorySerializer
from . import models


class MallSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    # categories = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='category-detail')

    class Meta:
        model = models.Mall
        # fields는 데이터베이스 속성을 제어합니다.
        fields = (
            'no',
            'member_no',
            'link',
            'tel',
            'email',
            'address',
            'name',
            'desc',
            'register_datetime',
            'update_information_datetime',
            'categories',
        )

