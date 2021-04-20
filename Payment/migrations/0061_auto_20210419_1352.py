# Generated by Django 3.1.6 on 2021-04-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0060_auto_20210307_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='MaximumAmount',
            field=models.BigIntegerField(blank=True, default=0, verbose_name='حداکثر مبلغ خرید'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='MinimumAmount',
            field=models.BigIntegerField(blank=True, default=0, verbose_name='حداقل مبلغ خرید'),
        ),
    ]
