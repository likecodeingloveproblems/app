# Generated by Django 2.2.6 on 2020-01-30 16:20

import Payment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0026_auto_20200130_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='SerialNumber',
            field=models.CharField(default=Payment.models.BuildCoponCode(8), max_length=30, verbose_name='سریال کوپن'),
        ),
    ]
