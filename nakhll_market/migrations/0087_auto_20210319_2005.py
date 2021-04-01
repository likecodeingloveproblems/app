# Generated by Django 3.1.6 on 2021-03-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0086_historicalproduct_historicalprofile_historicalshop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='Height_With_Packaging',
            field=models.IntegerField(default=0, verbose_name='ارتفاع محصول با بسته بندی (سانتی متر('),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='Length_With_Packaging',
            field=models.IntegerField(default=0, verbose_name='طول محصول با بسته بندی (سانتی متر('),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='Net_Weight',
            field=models.IntegerField(default=0, verbose_name='وزن خالص محصول (گرم)'),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='Weight_With_Packing',
            field=models.IntegerField(default=0, verbose_name='وزن محصول با بسته بندی (گرم)'),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='Width_With_Packaging',
            field=models.IntegerField(default=0, verbose_name='عرض محصول با بسته بندی (سانتی متر('),
        ),
        migrations.AlterField(
            model_name='product',
            name='Height_With_Packaging',
            field=models.IntegerField(default=0, verbose_name='ارتفاع محصول با بسته بندی (سانتی متر('),
        ),
        migrations.AlterField(
            model_name='product',
            name='Length_With_Packaging',
            field=models.IntegerField(default=0, verbose_name='طول محصول با بسته بندی (سانتی متر('),
        ),
        migrations.AlterField(
            model_name='product',
            name='Net_Weight',
            field=models.IntegerField(default=0, verbose_name='وزن خالص محصول (گرم)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Weight_With_Packing',
            field=models.IntegerField(default=0, verbose_name='وزن محصول با بسته بندی (گرم)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Width_With_Packaging',
            field=models.IntegerField(default=0, verbose_name='عرض محصول با بسته بندی (سانتی متر('),
        ),
    ]