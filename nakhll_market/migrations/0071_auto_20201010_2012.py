# Generated by Django 2.2.6 on 2020-10-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0070_auto_20200930_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='Bio',
            field=models.TextField(blank=True, verbose_name='معرفی حجره دار'),
        ),
    ]
