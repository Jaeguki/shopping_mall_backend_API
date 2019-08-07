from rest_framework import serializers

from . import models


class ItemOptionSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemOptionSize
        # fields는 데이터베이스 속성을 제어합니다.
        fields = (
            'no',
            'item_option_no',
            'name',
        )


class ItemOptionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemOptionImage
        # fields는 데이터베이스 속성을 제어합니다.
        fields = (
            'no',
            'item_option_no',
            'detail',
            'register_datetime',
            'update_datetime',
        )


class ItemOptionSerializer(serializers.ModelSerializer):
    images = ItemOptionImageSerializer(many=True, read_only=True)
    sizes = ItemOptionSizeSerializer(many=True, read_only=True)

    class Meta:
        model = models.ItemOption
        # fields는 데이터베이스 속성을 제어합니다.
        fields = (
            'no',
            'item_no',
            'detail',
            'desc',
            'sell_count',
            'cart_count',
            'register_datetime',
            'update_information_datetime',
            'images',
            'sizes',
        )


class ItemSerializer(serializers.ModelSerializer):
    options = ItemOptionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Item
        # fields는 데이터베이스 속성을 제어합니다.
        fields = (
            'no',
            'category_no',
            'name',
            'image',
            'desc',
            'price',
            'display_yn',
            'total_sell_count',
            'total_cart_count',
            'register_datetime',
            'update_information_datetime',
            'options',
        )
