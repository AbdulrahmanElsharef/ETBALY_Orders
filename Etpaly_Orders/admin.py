from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

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
    list_filter = ['code', 'status', 'customer__name',
                   'customer__phone', 'delivery_date']
    search_fields = ['customer__name', 'customer__phone']
    exclude = ('code','slug',)
    # Render filtered options only after 5 characters were entered

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

# @admin.register(StockItem)
# class StockItemAdmin(admin.ModelAdmin):
#     list_display = ['__str__', 'name', 'unit',
#                     'total_stock', 'limit', 'stock_limit']
#     list_filter = ['name', 'unit', 'unit']
#     search_fields = ['description']

#     def total_stock(self, instance):
#         return instance.stock_total()

#     def stock_limit(self, instance):
#         if instance.limit >= instance.stock_total():
#             return 'Good_Stock'
#         else:
#             return "Out_Stock"


# @admin.register(Stock_Transaction)
# class Stock_TransactionAdmin(admin.ModelAdmin):
#     list_display = ['item', 'name', 'stock_in', 'stock_out', 'quantity']
#     list_filter = ['item', 'Transaction']
#     search_fields = ['item', 'Transaction']

#     def name(self, obj):
#         return obj.item.name

#     def stock_in(self, obj):
#         if obj.Transaction == 'Stock_In':
#             return obj.Transaction

#     def stock_out(self, obj):
#         if obj.Transaction == 'Stock_Out':
#             return obj.Transaction
