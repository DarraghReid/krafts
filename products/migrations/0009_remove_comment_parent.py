# Generated by Django 3.2.7 on 2021-10-15 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]