# Generated by Django 3.2.7 on 2021-09-08 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, default='4348618274', max_length=254, null=True),
        ),
    ]
