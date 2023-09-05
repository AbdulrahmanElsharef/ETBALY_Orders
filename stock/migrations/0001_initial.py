# Generated by Django 4.2.4 on 2023-09-05 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('unit', models.CharField(choices=[('عدد', 'عدد'), ('كيلو', 'كيلو'), ('روزمة', 'روزمة')], max_length=50)),
                ('limit', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock_Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction', models.CharField(choices=[('Stock_In', 'Stock_In'), ('Stock_Out', 'Stock_Out')], max_length=50)),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Stock_Transaction', to='stock.stockitem', verbose_name='item')),
            ],
        ),
    ]
