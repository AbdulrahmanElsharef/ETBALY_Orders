# Generated by Django 4.2.4 on 2023-08-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etpaly_Orders', '0002_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
