from rest_framework import serializers

from cart.serializers import CartSerializer
from . import models


class NonMemberSerializer(serializers.ModelSerializer):
    carts = CartSerializer(many=True, read_only=True)

    class Meta:
        # fields는 데이터베이스 속성을 제어합니다.
        fields = (
            'no',
            'name',
            'phone',
            'password',
            'carts',
        )
        model = models.NonMember
