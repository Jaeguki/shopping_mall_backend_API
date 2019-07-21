from django.db import models

# Create your models here.
from category.models import Category


class Item(models.Model):
    no = models.BigAutoField(primary_key=True)
    category_no = models.ForeignKey(Category, models.DO_NOTHING, db_column='category_no')
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    hit_count = models.IntegerField()
    price = models.IntegerField()
    display_yn = models.BooleanField()
    total_sell_count = models.IntegerField()
    total_cart_count = models.IntegerField()
    register_datetime = models.DateTimeField(auto_now_add=True)
    update_information_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'item'

    def __str__(self):
        return f'no:{self.no}, name:{self.name}'
