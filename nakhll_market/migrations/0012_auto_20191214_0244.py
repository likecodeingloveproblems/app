# Generated by Django 2.2.6 on 2019-12-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0011_auto_20191213_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='Status',
            field=models.BooleanField(choices=[(True, 'ثبت تغییرات'), (False, 'عدم ثبت تغییرات')], null=True, verbose_name='وضعیت تغییرات'),
        ),
    ]
