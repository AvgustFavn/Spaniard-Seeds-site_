# Generated by Django 4.2.9 on 2024-01-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weed_site', '0008_delete_categories_user_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.TextField(null=True, unique=True),
        ),
    ]
