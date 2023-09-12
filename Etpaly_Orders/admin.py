from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','details']
    list_filter = ['name',  ]
    search_fields = ['name',  ]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['company','client', 'phone_1','phone_2', 'location']
    list_filter = ['company','client', 'phone_1','phone_2' ]
    search_fields=['location',]
# __________________________________________________________


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    list_filter = ['name', 'phone']

# __________________________________________________________

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    list_filter = ['name', 'phone']

# __________________________________________________________
class OrderDetailInline(admin.TabularInline):
    model = OrderDetail


@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]
    list_display = ['__str__','branch','status','seller','active','customer','designer','order_date_','items','Total_','transfer','cash','Debit','Due_date_',]
    list_filter = ['id','branch','status','seller__name','active','customer','designer__name','order_date','Due_date',]
    search_fields = ['customer', 'customer__phone']




    def Total_(self, instance):
        return instance.net_total()
    
    def Debit(self, instance):
        return instance.Customer_debt()

    def items(self, instance):
        return instance.total_items()


    def order_date_(self, obj):
        if obj.order_date:
            return obj.order_date.strftime('%d-%m-%Y')
    
    def Due_date_(self, obj):
        if obj.Due_date:
            return obj.Due_date.strftime('%d-%m-%Y')


# __________________________________________________________

