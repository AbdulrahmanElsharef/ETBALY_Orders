from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# class TransactionInline(admin.TabularInline):
#     model = Transaction
    
@admin.register(StockItem)
class StockItemAdmin(ImportExportModelAdmin):
    # inlines = [TransactionInline]
    list_display = ['code','__str__','category','unit','price','stock_total','stock_price','created_at']
    list_filter = ['id','name','category__name','unit__name','created_at',]
    search_fields = ['name','description','category']

@admin.register(Transaction)
class Transactiondmin(ImportExportModelAdmin):
    list_display = ['transaction','officer',"item",'quantity','date']
    list_filter = ['transaction','officer',"item",'quantity','date']
    search_fields = ["item",'transaction','quantity']

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ["name",'note']
    list_filter = ["name"]
    search_fields = ["name"]
    
@admin.register(UOM)
class UOMAdmin(ImportExportModelAdmin):
    list_display = ["name",'note']
    list_filter = ["name"]
    search_fields = ["name"]
    
@admin.register(Officer)
class Officerdmin(ImportExportModelAdmin):
    list_display = ["name",'phone','note']
    list_filter = ["name"]
    search_fields = ["name"]

