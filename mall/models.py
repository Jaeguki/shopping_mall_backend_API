from django.db import models

# Create your models here.
from member.models import Member


class Mall(models.Model):
    no = models.BigAutoField(primary_key=True)
    member_no = models.ForeignKey(Member, related_name='malls', on_delete=models.DO_NOTHING, db_column='member_no')
    link = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    tel = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, default='')
    address = models.CharField(max_length=255, default='')
    register_datetime = models.DateTimeField(auto_now_add=True)
    update_information_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mall'

    def __str__(self):
        return f'no:{self.no}, name:{self.name}'

