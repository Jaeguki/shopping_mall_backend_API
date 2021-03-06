# Generated by Django 2.2.3 on 2019-07-25 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('non_member', '0001_initial'),
        ('member', '0001_initial'),
        ('shipping', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('no', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
                ('register_datetime', models.DateTimeField(auto_now_add=True)),
                ('update_information_datetime', models.DateTimeField(auto_now=True)),
                ('desc', models.CharField(max_length=1024)),
                ('message', models.CharField(max_length=100)),
                ('total_quantity', models.PositiveSmallIntegerField()),
                ('payment_type', models.CharField(max_length=100)),
                ('member_no', models.ForeignKey(blank=True, db_column='member_no', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='member.Member')),
                ('non_member_no', models.ForeignKey(db_column='non_member_no', on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='non_member.NonMember')),
                ('shipping_no', models.ForeignKey(db_column='shipping_no', on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='shipping.Shipping')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
