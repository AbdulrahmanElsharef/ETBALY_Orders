# Generated by Django 4.2.4 on 2023-09-05 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etpaly_Orders', '0002_rename_sellers_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_1',
            field=models.CharField(default='', max_length=14, verbose_name='Phone 1 '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_2',
            field=models.CharField(default='', max_length=14, verbose_name='Phone 2 '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.TextField(default='No_Details', max_length=300, verbose_name='Details'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Delivery',
            field=models.IntegerField(default=0, verbose_name='Delivery'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cash',
            field=models.IntegerField(default=0, verbose_name='Cash'),
        ),
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.IntegerField(default=0, verbose_name='Discount'),
        ),
        migrations.AlterField(
            model_name='order',
            name='transfer',
            field=models.IntegerField(default=0, verbose_name='Transfer'),
        ),
    ]