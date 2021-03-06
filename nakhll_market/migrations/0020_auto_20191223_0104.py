# Generated by Django 2.2.6 on 2019-12-22 21:34

from django.db import migrations, models
import nakhll_market.models


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0019_remove_shop_newimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='NewImage',
            field=models.ImageField(blank=True, null=True, upload_to=nakhll_market.models.PathAndRename('media/Pictures/Markets/SubMarkets/Shops/Products/'), verbose_name='عکس جدید حجره'),
        ),
        migrations.AddField(
            model_name='productbanner',
            name='NewImage',
            field=models.ImageField(blank=True, null=True, upload_to=nakhll_market.models.PathAndRename('media/Pictures/Markets/SubMarkets/Shops/Products/Banners/'), verbose_name='عکس جدید حجره'),
        ),
        migrations.AddField(
            model_name='shop',
            name='NewImage',
            field=models.ImageField(blank=True, null=True, upload_to=nakhll_market.models.PathAndRename('media/Pictures/Markets/SubMarkets/Shops/'), verbose_name='عکس جدید حجره'),
        ),
        migrations.AddField(
            model_name='shopbanner',
            name='NewImage',
            field=models.ImageField(blank=True, null=True, upload_to=nakhll_market.models.PathAndRename('media/Pictures/Markets/SubMarkets/Shops/Banners'), verbose_name='عکس جدید حجره'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='Publish',
            field=models.BooleanField(choices=[(True, 'منتشر شده'), (False, 'در انتظار تایید')], default=False, verbose_name='وضعیت انتشار ویژگی'),
        ),
        migrations.AlterField(
            model_name='attrproduct',
            name='Available',
            field=models.BooleanField(choices=[(True, 'نمایش ویژگی'), (False, 'عدم نمایش ویژگی')], default=False, verbose_name='وضعیت ویژگی'),
        ),
    ]
