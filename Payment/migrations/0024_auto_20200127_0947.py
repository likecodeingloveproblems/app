# Generated by Django 2.2.6 on 2020-01-27 06:17

import Payment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0023_auto_20200126_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='SerialNumber',
            field=models.CharField(default=Payment.models.BuildCoponCode(11), max_length=11, unique=True, verbose_name='سریال کوپن'),
        ),
    ]
