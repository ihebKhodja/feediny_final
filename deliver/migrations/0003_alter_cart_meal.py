# Generated by Django 3.2.4 on 2021-06-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliver', '0002_cart_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='meal',
            field=models.ManyToManyField(null=True, to='deliver.Meal'),
        ),
    ]