from django.db import models
from member.models import Member
from non_member.models import NonMember


class Shipping(models.Model):
    no = models.BigAutoField(primary_key=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no', blank=True, null=True)
    non_member_no = models.ForeignKey(NonMember, models.DO_NOTHING, db_column='non_member_no', blank=True, null=True)
    name = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=7)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    address4 = models.CharField(max_length=100, blank=True, null=True)
    information = models.CharField(max_length=100, blank=True, null=True)
    register_datetime = models.DateTimeField(auto_now_add=True)
    update_information_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shipping'
