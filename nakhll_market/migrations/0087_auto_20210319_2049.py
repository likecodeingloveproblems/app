# Generated by Django 3.1.6 on 2021-03-19 17:19
from django.db import migrations, models
from nakhll_market.models import Product

def make_int(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    products = Product.objects.all()
    for product in products:
        product.Net_Weight = round(float(product.Net_Weight))
        product.Weight_With_Packing = round(float(product.Weight_With_Packing))
        product.Length_With_Packaging = round(float(product.Length_With_Packaging))
        product.Width_With_Packaging = round(float(product.Width_With_Packaging))
        product.Height_With_Packaging = round(float(product.Height_With_Packaging))
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0086_historicalproduct_historicalprofile_historicalshop'),
    ]

    operations = [
        migrations.RunPython(make_int),
    ]
