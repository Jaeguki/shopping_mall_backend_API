from rest_framework import serializers

from cart.serializers import CartSerializer
from mall.serializers import MallSerializer
from . import models


class MemberSerializer(serializers.ModelSerializer):
    malls = MallSerializer(many=True, read_only=True)
    carts = CartSerializer(many=True, read_only=True)
    class Meta:
        # 해당하는 모델
        model = models.Member

        # 직렬화시 포함시키지 않을 데이터
        extra_kwargs = {'password': {'write_only': True}}

        # fields는 데이터베이스 속성을 제어합니다.
        fields = (
            'no',
            'id',
            'password',
            'email',
            'password',
            'last_name',
            'first_name',
            'phone',
            'birthday',
            'sex',
            'register_datetime',
            'icon',
            'photo',
            'update_information_datetime',
            'last_login_datetime',
            'seller_cert_yn',
            'seller_yn',
            'receive_email_yn',
            'receive_sms_yn',
            'email_cert_yn',
            'denied_yn',
            'activation_yn',
            'malls',
            'carts',
        )

