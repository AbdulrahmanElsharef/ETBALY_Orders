from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'unit',
                    'total_stock', 'limit', 'stock_limit']
    list_filter = ['name', 'unit', 'updated_at']
    search_fields = ['name','description']

    def total_stock(self, instance):
        return instance.stock_total()

    def stock_limit(self, instance):
        if instance.limit >= instance.stock_total():
            return 'Good_Stock'
        else:
            return "Out_Stock"


@admin.register(Stock_Transaction)
class Stock_TransactionAdmin(admin.ModelAdmin):
    list_display = ['item', 'name', 'stock_in', 'stock_out', 'quantity']
    list_filter = ['item__name', 'Transaction']
    search_fields = ['item__name',]

    def name(self, obj):
        return obj.item.name

    def stock_in(self, obj):
        if obj.Transaction == 'Stock_In':
            return obj.Transaction

    def stock_out(self, obj):
        if obj.Transaction == 'Stock_Out':
            return obj.Transaction
