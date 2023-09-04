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
class OrderDetailInline(admin.TabularInline):
    model = OrderDetail


@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]
    list_display = ['__str__','branch','status','active','customer','PHONE','designer','order_date','discount','Delivery','Total_','delivery_date']
    list_filter = ['id','branch','status','active','customer','customer__phone','order_date','delivery_date']
    search_fields = ['customer', 'customer__phone']
    # exclude=('id','note')


    def PHONE(self, instance):
        return instance.customer.phone



    def Total_(self, instance):
        return instance.net_total()



# __________________________________________________________

