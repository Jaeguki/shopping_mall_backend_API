# Generated by Django 2.2.3 on 2019-07-23 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_itemoption_itemoptionimage_itemoptionsize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='display_yn',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='hit_count',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='total_cart_count',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='total_sell_count',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='itemoption',
            name='cart_count',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='itemoption',
            name='sell_count',
            field=models.PositiveSmallIntegerField(),
        ),
    ]