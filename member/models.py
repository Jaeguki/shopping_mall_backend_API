from django.db import models


# Create your models here.


class Member(models.Model):
    no = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    id = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    birthday = models.CharField(max_length=10)
    sex = models.BooleanField(default=True)
    register_datetime = models.DateTimeField(auto_now_add=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    update_information_datetime = models.DateTimeField(auto_now=True)
    last_login_datetime = models.DateTimeField(blank=True, null=True)
    seller_cert_yn = models.BooleanField(default=False)
    seller_yn = models.BooleanField(default=False)
    receive_email_yn = models.BooleanField(default=False)
    receive_sms_yn = models.BooleanField(default=False)
    email_cert_yn = models.BooleanField(default=False)
    denied_yn = models.BooleanField(default=False)
    activation_yn = models.BooleanField(default=False)

    class Meta:
        db_table = 'member'

    def __str__(self):
        return f'no: {self.no}, id:{self.id}'


