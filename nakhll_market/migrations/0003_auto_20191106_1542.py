# Generated by Django 2.2.6 on 2019-11-06 12:12

from django.db import migrations, models
import nakhll_market.models


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0002_auto_20191106_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='IPAddress',
            field=models.CharField(blank=True, max_length=15, verbose_name='آدرس ای پی'),
        ),
        migrations.AlterField(
            model_name='submarket',
            name='Image',
            field=models.ImageField(blank=True, help_text='عکس مورد نظر را اینجا وارد کنید', null=True, upload_to=nakhll_market.models.PathAndRename('media/Pictures/Markets/SubMarkets/'), verbose_name='عکس راسته'),
        ),
    ]
