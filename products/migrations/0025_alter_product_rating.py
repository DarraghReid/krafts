# Generated by Django 3.2.7 on 2021-10-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]