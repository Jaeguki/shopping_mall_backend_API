from rest_framework import serializers
from . import models


class ItemSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many=True, read_only=True)
    # categories = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='category-detail')

    class Meta:
        model = models.Item
        # fields는 데이터베이스 속성을 제어합니다.
        fields = (
            'no',
            'category_no',
            'name',
            'image',
            'desc',
            'hit_count',
            'price',
            'display_yn',
            'total_sell_count',
            'total_cart_count',
            'register_datetime',
            'update_information_datetime',
        )
