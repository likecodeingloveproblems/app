# Generated by Django 3.1.6 on 2021-03-23 21:45

from django.db import migrations, models
from nakhll_market.models import Product

def fill_discount(apps, schema_editor):
    products = Product.objects.exclude(OldPrice=0)
    for product in products:
        price = product.Price
        old_price = product.OldPrice
        discount = old_price - price
        product.discount = discount
        product.Price = old_price
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0089_auto_20210324_0215'),
    ]

    operations = [
        migrations.RunPython(fill_discount),
    ]
