# Generated by Django 3.2.4 on 2021-06-12 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliver', '0008_restaurant_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='owner',
        ),
    ]
