# Generated by Django 4.2 on 2023-08-11 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Etpaly_Orders', '0006_stock_transaction_remove_stockout_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='total',
        ),
        migrations.AlterField(
            model_name='stock_transaction',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Stock_Transaction', to='Etpaly_Orders.stockitem', verbose_name='item'),
        ),
    ]
