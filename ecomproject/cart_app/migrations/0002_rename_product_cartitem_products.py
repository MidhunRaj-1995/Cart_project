# Generated by Django 4.2.8 on 2023-12-21 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product',
            new_name='products',
        ),
    ]
