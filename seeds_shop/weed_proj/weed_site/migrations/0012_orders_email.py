# Generated by Django 4.2.9 on 2024-01-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weed_site', '0011_rename_full_name_orders_name_orders_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.TextField(null=True),
        ),
    ]
