# Generated by Django 3.2.7 on 2021-10-21 19:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0033_alter_product_rates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rates',
            field=models.ManyToManyField(blank=True, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
