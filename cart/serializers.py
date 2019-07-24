from rest_framework import serializers

from . import models


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        # fields는 데이터베이스 속성을 제어합니다.
        fields =(
            'no',
            'member_no',
            'non_member_no',
            'item_option_size_no',
            'item_quantity',
        )
        model = models.Cart


