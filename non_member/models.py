from django.db import models

# Create your models here.
from order.models import Order


class NonMember(models.Model):
    no = models.IntegerField(primary_key=True)
    order_no = models.ForeignKey(Order, models.DO_NOTHING, db_column='order_no')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'non_member'

    def __str__(self):
        return f'no:{self.no}, order_no:{self.order_no}'
