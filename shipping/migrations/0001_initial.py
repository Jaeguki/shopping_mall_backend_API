# Generated by Django 2.2.3 on 2019-07-25 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
        ('non_member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('no', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('recipient', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=7)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('address3', models.CharField(blank=True, max_length=100, null=True)),
                ('address4', models.CharField(blank=True, max_length=100, null=True)),
                ('information', models.CharField(blank=True, max_length=100, null=True)),
                ('register_datetime', models.DateTimeField(auto_now_add=True)),
                ('update_information_datetime', models.DateTimeField(auto_now=True)),
                ('member_no', models.ForeignKey(blank=True, db_column='member_no', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='member.Member')),
                ('non_member_no', models.ForeignKey(blank=True, db_column='non_member_no', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='non_member.NonMember')),
            ],
            options={
                'db_table': 'shipping',
            },
        ),
    ]
