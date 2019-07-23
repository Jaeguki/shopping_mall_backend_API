from django.db import models

# Create your models here.
from member.models import Member
from shipping.models import Shipping


class Order(models.Model):
    no = models.BigAutoField(primary_key=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no', blank=True, null=True)
    shipping_no = models.ForeignKey(Shipping, models.DO_NOTHING, db_column='shipping_no')
    status = models.CharField(max_length=100)
    register_datetime = models.DateTimeField(auto_now_add=True)
    update_information_datetime = models.DateTimeField(auto_now=True)
    desc = models.CharField(max_length=1024)
    message = models.CharField(max_length=100)
    total_quantity = models.PositiveSmallIntegerField()
    payment_type = models.CharField(max_length=100)

    class Meta:
        db_table = 'order'

