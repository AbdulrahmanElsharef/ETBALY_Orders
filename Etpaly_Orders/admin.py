from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',   'subtitle']
    list_filter = ['name',  ]
    search_fields = ['name',  ]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['company','client', 'phone', 'location']
    list_filter = ['company','client', 'phone', ]
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
    list_display = ['__str__','branch','status','Seller','active','customer','designer','order_date','Total_','cash','transfer','Client_Debit','Due_date',]
    list_filter = ['id','branch','status','Seller','active','customer','designer','order_date','Due_date',]
    search_fields = ['customer', 'customer__phone']




    def Total_(self, instance):
        return instance.net_total()
    
    def Client_Debit(self, instance):
        return instance.Customer_debt()




# __________________________________________________________

