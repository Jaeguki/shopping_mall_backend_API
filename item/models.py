from django.db import models

# Create your models here.
from category.models import Category


class Item(models.Model):
    no = models.BigAutoField(primary_key=True)
    category_no = models.ForeignKey(Category, related_name='items', on_delete=models.DO_NOTHING, db_column='category_no')
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=200)
    desc = models.CharField(max_length=1000)
    hit_count = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField()
    display_yn = models.BooleanField(default=False)
    total_sell_count = models.PositiveSmallIntegerField()
    total_cart_count = models.PositiveSmallIntegerField()
    register_datetime = models.DateTimeField(auto_now_add=True)
    update_information_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'item'

    def __str__(self):
        return f'no:{self.no}, name:{self.name}'


class ItemOption(models.Model):
    no = models.BigAutoField(primary_key=True)
    item_no = models.ForeignKey(Item, related_name='options', on_delete=models.DO_NOTHING, db_column='item_no')
    detail = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    sell_count = models.PositiveSmallIntegerField()
    cart_count = models.PositiveSmallIntegerField()
    register_datetime = models.DateTimeField(auto_now_add=True)
    update_information_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'item_option'

    def __str__(self):
        return f'no:{self.no}, detail:{self.detail}'


class ItemOptionImage(models.Model):
    no = models.BigAutoField(primary_key=True)
    item_option_no = models.ForeignKey(ItemOption, related_name='images', on_delete=models.DO_NOTHING, db_column='item_option_no')
    detail = models.URLField(max_length=200)
    register_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'item_option_image'

    def __str__(self):
        return f'no:{self.no}, detail:{self.detail}'


class ItemOptionSize(models.Model):
    no = models.BigAutoField(primary_key=True)
    item_option_no = models.ForeignKey(ItemOption, related_name='sizes', on_delete=models.DO_NOTHING, db_column='item_option_no')
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'item_option_size'
        unique_together = (('no', 'item_option_no'),)

    def __str__(self):
        return f'no:{self.no}, name:{self.name}'
