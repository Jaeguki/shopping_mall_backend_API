from rest_framework import serializers

from . import models


class ShippingSerializer(serializers.ModelSerializer):

    class Meta:
        # fields는 데이터베이스 속성을 제어합니다.
        fields = (
            'no',
            'member_no',
            'non_member_no',
            'name',
            'recipient',
            'phone',
            'zipcode',
            'address1',
            'address2',
            'address3',
            'address4',
            'information',
            'register_datetime',
            'update_information_datetime',
        )
        model = models.Shipping

