from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',  'sku', 'subtitle']
    list_filter = ['name', 'sku', ]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'location']
    list_filter = ['name', 'phone', ]
# __________________________________________________________


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail


@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]
    list_display = ['__str__', 'status','customer',
                    'delivery_date', 'sup', 'Delivery_Fee', 'discount', 'total_order']
    list_filter = ['id', 'status', 'customer__name',
                   'customer__phone', 'delivery_date']
    search_fields = ['customer__name', 'customer__phone']


    def customer(self, instance):
        return instance.customer.name



    def total_order(self, instance):
        return instance.net_total()

    def sup(self, instance):
        return instance.sup_total()


# __________________________________________________________

