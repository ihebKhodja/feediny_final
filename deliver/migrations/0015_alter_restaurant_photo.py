# Generated by Django 3.2.4 on 2021-06-13 10:55

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliver', '0014_alter_cart_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
