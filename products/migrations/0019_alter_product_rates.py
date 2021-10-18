# Generated by Django 3.2.7 on 2021-10-17 16:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0018_alter_product_rates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rates',
            field=models.ManyToManyField(related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]