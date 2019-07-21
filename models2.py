# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cart(models.Model):
    no = models.BigAutoField(primary_key=True)
    member_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_no', blank=True, null=True)
    non_member_no = models.ForeignKey('NonMember', models.DO_NOTHING, db_column='non_member_no', blank=True, null=True)
    item_option_no = models.BigAutoField()
    item_option_size_no = models.ForeignKey('ItemOptionSize', models.DO_NOTHING, db_column='item_option_size_no')
    item_choice_count = models.IntegerField()
    item_register_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cart'


class Category(models.Model):
    no = models.BigAutoField(primary_key=True)
    mall_no = models.ForeignKey('Mall', models.DO_NOTHING, db_column='mall_no')
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    register_datetime = models.DateTimeField()
    update_information_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category'


class Item(models.Model):
    no = models.BigAutoField(primary_key=True)
    category_no = models.ForeignKey(Category, models.DO_NOTHING, db_column='category_no')
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    hit_count = models.BigAutoField()
    price = models.IntegerField()
    display_yn = models.BooleanField()
    total_sell_count = models.IntegerField()
    total_cart_count = models.IntegerField()
    register_datetime = models.DateTimeField()
    update_information_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'item'


class ItemOption(models.Model):
    no = models.BigAutoField(primary_key=True)
    item_no = models.ForeignKey(Item, models.DO_NOTHING, db_column='item_no')
    detail = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    sell_count = models.IntegerField()
    cart_count = models.IntegerField()
    register_datetime = models.DateTimeField()
    update_information_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'item_option'


class ItemOptionImage(models.Model):
    no = models.BigAutoField(primary_key=True)
    item_option_no = models.ForeignKey(ItemOption, models.DO_NOTHING, db_column='item_option_no')
    detail = models.CharField(max_length=1000)
    register_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'item_option_image'


class ItemOptionSize(models.Model):
    no = models.BigAutoField(primary_key=True)
    item_option_no = models.ForeignKey(ItemOption, models.DO_NOTHING, db_column='item_option_no')
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'item_option_size'
        unique_together = (('no', 'item_option_no'),)


class Mall(models.Model):
    no = models.BigAutoField(primary_key=True)
    member_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_no')
    link = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    register_datetime = models.DateTimeField()
    update_information_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mall'


class Member(models.Model):
    no = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    birthday = models.CharField(max_length=10)
    sex = models.BooleanField()
    register_datetime = models.DateTimeField()
    icon = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    update_information_datetime = models.DateTimeField()
    last_login_datetime = models.DateTimeField(blank=True, null=True)
    seller_cert_yn = models.BooleanField()
    seller_yn = models.BooleanField()
    receive_email_yn = models.BooleanField()
    receive_sms_yn = models.BooleanField()
    email_cert_yn = models.BooleanField()
    denied_yn = models.BooleanField()
    activation_yn = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'member'


class NonMember(models.Model):
    no = models.IntegerField(primary_key=True)
    order_no = models.ForeignKey('Order', models.DO_NOTHING, db_column='order_no')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'non_member'


class Order(models.Model):
    no = models.BigAutoField(primary_key=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no', blank=True, null=True)
    shipping_no = models.ForeignKey('Shipping', models.DO_NOTHING, db_column='shipping_no')
    status = models.CharField(max_length=100)
    register_datetime = models.DateTimeField()
    update_information_datetime = models.DateTimeField()
    desc = models.CharField(max_length=1024)
    message = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    payment_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'order'


class OrderItem(models.Model):
    order_item_no = models.BigAutoField(primary_key=True)
    order_no = models.ForeignKey(Order, models.DO_NOTHING, db_column='order_no')
    item_option_size_no = models.ForeignKey(ItemOptionSize, models.DO_NOTHING, db_column='item_option_size_no')
    item_option_no = models.BigAutoField()
    count = models.IntegerField()
    total_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_item'


class Shipping(models.Model):
    no = models.BigAutoField(primary_key=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no', blank=True, null=True)
    name = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=7)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    address4 = models.CharField(max_length=100, blank=True, null=True)
    information = models.CharField(max_length=100, blank=True, null=True)
    register_datetime = models.DateTimeField()
    update_information_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shipping'
