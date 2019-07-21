from django.db import models

# Create your models here.
from mall.models import Mall


class Category(models.Model):
    no = models.BigAutoField(primary_key=True)
    mall_no = models.ForeignKey(Mall, related_name='categories', on_delete=models.DO_NOTHING, db_column='mall_no')
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    register_datetime = models.DateTimeField(auto_now_add=True)
    update_information_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f'no:{self.no}, name:{self.name}'
