# Generated by Django 4.2 on 2023-08-10 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Etpaly_Orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='address',
            new_name='location',
        ),
    ]
