# Generated by Django 4.2.9 on 2024-01-18 16:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weed_site', '0012_orders_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
    ]