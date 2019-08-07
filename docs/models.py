# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cart(models.Model):
    cart_no = models.BigAutoField(primary_key=True)
    member_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_no', blank=True, null=True)
    item_no = models.ForeignKey('Item', models.DO_NOTHING, db_column='item_no')
    cart_item_choice_count = models.IntegerField()
    cart_item_register_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Category(models.Model):
    category_no = models.BigAutoField(primary_key=True)
    mall_no = models.ForeignKey('Mall', models.DO_NOTHING, db_column='mall_no')
    category_name = models.CharField(max_length=100)
    category_desc = models.CharField(max_length=255)
    category_register_datetime = models.DateTimeField(auto_now_add=True)
    category_update_information_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'category'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField(auto_now_add=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'django_session'


class Item(models.Model):
    item_no = models.BigAutoField(primary_key=True)
    category_no = models.ForeignKey(Category, models.DO_NOTHING, db_column='category_no')
    item_name = models.CharField(max_length=100)
    item_image = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=1000)
    item_hit_count = models.BigAutoField()
    item_price = models.IntegerField()
    item_total_sell_count = models.IntegerField()
    item_total_cart_count = models.IntegerField()
    item_register_datetime = models.DateTimeField(auto_now_add=True)
    item_update_information_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'item'


class ItemOption(models.Model):
    item_option_no = models.BigAutoField(primary_key=True)
    item_no = models.ForeignKey(Item, models.DO_NOTHING, db_column='item_no')
    item_detail_option = models.CharField(max_length=1000)
    item_option_desc = models.CharField(max_length=1000)
    item_option_sell_count = models.IntegerField()
    item_option_cart_count = models.IntegerField()
    item_option_register_datetime = models.DateTimeField(auto_now_add=True)
    item_option_update_information_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'item_option'


class ItemOptionImage(models.Model):
    item_option_image_no = models.BigAutoField(primary_key=True)
    item_option_no = models.ForeignKey(ItemOption, models.DO_NOTHING, db_column='item_option_no')
    item_option_image_detail = models.CharField(max_length=1000)
    item_option_image_register_datetime = models.DateTimeField(auto_now_add=True)
    item_option_image_update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'item_option_image'


class ItemOptionSize(models.Model):
    item_option_size_no = models.BigAutoField(primary_key=True)
    item_option_no = models.ForeignKey(ItemOption, models.DO_NOTHING, db_column='item_option_no')
    item_option_size_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'item_option_size'
        unique_together = (('item_option_size_no', 'item_option_no'),)


class Mall(models.Model):
    mall_no = models.BigAutoField(primary_key=True)
    member_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_no')
    mall_link = models.CharField(max_length=255)
    mall_name = models.CharField(max_length=100)
    mall_desc = models.CharField(max_length=255)
    mall_register_datetime = models.DateTimeField(auto_now_add=True)
    mall_update_information_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'mall'


class Member(models.Model):
    member_no = models.IntegerField(primary_key=True)
    member_id = models.CharField(max_length=100)
    member_email = models.CharField(max_length=255)
    member_password = models.CharField(max_length=255)
    member_lastname = models.CharField(max_length=100)
    member_firstname = models.CharField(max_length=100)
    member_phone = models.CharField(max_length=100)
    member_birthday = models.CharField(max_length=10)
    member_sex = models.BooleanField()
    member_register_datetime = models.DateTimeField(auto_now_add=True)
    member_icon = models.CharField(max_length=255, blank=True, null=True)
    member_photo = models.CharField(max_length=255, blank=True, null=True)
    member_update_information_datetime = models.DateTimeField(auto_now=True)
    member_lastlogin_datetime = models.DateTimeField(blank=True, null=True)
    member_is_seller_cert = models.BooleanField()
    member_is_seller = models.BooleanField()
    member_receive_email = models.BooleanField()
    member_receive_sms = models.BooleanField()
    member_email_cert = models.BooleanField()
    member_denied = models.BooleanField()
    member_is_activation = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'member'


class NonMember(models.Model):
    order_no = models.ForeignKey('Order', models.DO_NOTHING, db_column='order_no', primary_key=True)
    non_mem_name = models.CharField(max_length=100)
    non_mem_phone = models.CharField(max_length=100)
    non_mem_password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'non_member'


class Order(models.Model):
    order_no = models.BigAutoField(primary_key=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no', blank=True, null=True)
    shipping_no = models.ForeignKey('Shipping', models.DO_NOTHING, db_column='shipping_no')
    order_status = models.CharField(max_length=100)
    order_register_datetime = models.DateTimeField(auto_now_add=True)
    order_update_information_datetime = models.DateTimeField(auto_now=True)
    order_desc = models.CharField(max_length=1024)
    order_message = models.CharField(max_length=100)
    order_total_amount = models.IntegerField()
    order_payment_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'order'


class OrderItem(models.Model):
    order_item_no = models.BigAutoField(primary_key=True)
    order_no = models.ForeignKey(Order, models.DO_NOTHING, db_column='order_no')
    item_option_size_no = models.ForeignKey(ItemOptionSize, models.DO_NOTHING, db_column='item_option_size_no')
    item_option_no = models.BigAutoField()
    order_item_count = models.IntegerField()
    order_item_total_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_item'


class Shipping(models.Model):
    shipping_no = models.BigAutoField(primary_key=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no', blank=True, null=True)
    shipping_name = models.CharField(max_length=100)
    shipping_recipient = models.CharField(max_length=100)
    shipping_phone = models.CharField(max_length=100)
    shipping_zipcode = models.CharField(max_length=7)
    shipping_address1 = models.CharField(max_length=100)
    shipping_address2 = models.CharField(max_length=100, blank=True, null=True)
    shipping_address3 = models.CharField(max_length=100, blank=True, null=True)
    shipping_address4 = models.CharField(max_length=100, blank=True, null=True)
    shipping_information = models.CharField(max_length=100, blank=True, null=True)
    shipping_register_datetime = models.DateTimeField(auto_now_add=True)
    shipping_update_information_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'shipping'
