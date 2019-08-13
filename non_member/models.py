from django.db import models

# Create your models here.


class NonMember(models.Model):
    no = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'non_member'

    def __str__(self):
        return f'no:{self.no}, order_no:{self.order_no}'
