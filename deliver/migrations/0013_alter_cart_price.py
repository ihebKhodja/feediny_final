# Generated by Django 3.2.4 on 2021-06-12 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliver', '0012_auto_20210612_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]
