from django.db import models


# Create your models here.
from item.models import ItemOptionSize
from order.models import Order


class OrderItem(models.Model):
    no = models.BigAutoField(primary_key=True)
    order_no = models.ForeignKey(Order, related_name='order_items', on_delete=models.DO_NOTHING, db_column='order_no')
    item_option_size_no = models.ForeignKey(ItemOptionSize, related_name='order_items', on_delete=models.DO_NOTHING,
                                            db_column='item_option_size_no')
    count = models.PositiveIntegerField()
    total_amount = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'order_item'
