# Generated by Django 4.2 on 2023-08-11 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Etpaly_Orders', '0008_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='code',
        ),
    ]
