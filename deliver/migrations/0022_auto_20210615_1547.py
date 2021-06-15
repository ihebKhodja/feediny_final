# Generated by Django 3.2.4 on 2021-06-15 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210609_1544'),
        ('deliver', '0021_auto_20210615_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.client'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.client'),
        ),
    ]
