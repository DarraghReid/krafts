# Generated by Django 3.2.7 on 2021-10-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=1),
        ),
    ]