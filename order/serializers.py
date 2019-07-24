from rest_framework import serializers

from order_item.serializers import OrderItemSerializer
from . import models


class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        # fields는 데이터베이스 속성을 제어합니다.
        fields = (
            'no',
            'member_no',
            'shipping_no',
            'status',
            'register_datetime',
            'update_information_datetime',
            'desc',
            'message',
            'total_quantity',
            'payment_type',
            'orders',
        )
        model = models.Member

