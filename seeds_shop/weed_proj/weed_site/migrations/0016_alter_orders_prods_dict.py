# Generated by Django 4.2.9 on 2024-01-18 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weed_site', '0015_orders_prods_dict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='prods_dict',
            field=models.JSONField(default={}),
        ),
    ]
