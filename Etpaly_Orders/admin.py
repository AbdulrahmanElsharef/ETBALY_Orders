from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'sku', 'subtitle']
    list_filter = ['name', 'price', 'sku', ]

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
    list_display = ['__str__', 'status','customer','client_phone', 
                    'delivery_date', 'sup', 'Delivery_Fee', 'discount_', 'total_order']
    list_filter = ['id', 'status', 'customer__name',
                   'customer__phone', 'delivery_date']
    search_fields = ['customer__name', 'customer__phone']


    def customer(self, instance):
        return instance.customer.name

    def client_phone(self, instance):
        return instance.customer.phone

    def total_order(self, instance):
        return instance.net_total()

    def sup(self, instance):
        return instance.sup_total()

    def discount_(self, instance):
        dis = instance.sup_total*instance.discount/100
        return dis


# __________________________________________________________

