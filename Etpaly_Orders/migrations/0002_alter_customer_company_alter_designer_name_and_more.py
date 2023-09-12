# Generated by Django 4.2 on 2023-09-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etpaly_Orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='company',
            field=models.CharField(max_length=100, unique=True, verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='designer',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Designer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Seller'),
        ),
    ]
