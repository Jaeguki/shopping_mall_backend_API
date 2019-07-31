from rest_framework import serializers

from . import models


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        # fields는 데이터베이스 속성을 제어합니다.
        fields = (
            'no',
            'order_no',
            'item_option_size_no',
            'count',
            'total_amount',
        )
        model = models.OrderItem

