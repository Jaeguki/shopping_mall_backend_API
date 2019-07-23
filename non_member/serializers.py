from rest_framework import serializers

from . import models


class NonMemberSerializer(serializers.ModelSerializer):

    class Meta:
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
        )
        model = models.Member

