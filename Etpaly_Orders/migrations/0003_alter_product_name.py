# Generated by Django 4.2 on 2023-09-11 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etpaly_Orders', '0002_alter_customer_company_alter_designer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Product'),
        ),
    ]
