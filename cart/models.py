from django.db import models

from item.models import ItemOptionSize
from member.models import Member
from non_member.models import NonMember


class Cart(models.Model):
    no = models.BigAutoField(primary_key=True)
    member_no = models.ForeignKey(Member, related_name='carts', on_delete=models.DO_NOTHING,
                                  db_column='member_no', blank=True, null=True)
    non_member_no = models.ForeignKey(NonMember, related_name='carts', on_delete=models.DO_NOTHING,
                                      db_column='non_member_no', blank=True, null=True)
    item_option_size_no = models.ForeignKey(ItemOptionSize, models.DO_NOTHING, db_column='item_option_size_no')
    item_quantity = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return f'no:{self.no}, member_no:{self.member_no}, non_member_no:{self.non_member_no}, ' \
            f'item_option_size_no:{self.item_option_size_no}, item_quantity:{self.item_quantity}'
