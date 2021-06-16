# Generated by Django 3.2.4 on 2021-06-15 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210609_1544'),
        ('deliver', '0025_remove_restaurant_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.manager'),
        ),
    ]