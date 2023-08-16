from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','name','price','sku','subtitle','flag']
    
@admin.register(Customer) 
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['__str__','name','phone','location']
# __________________________________________________________

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail

@admin.register(Order) 
class orderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]
    list_display=['__str__','status','customer_name','delivery_time','total','dis_count','Delivery_Fee','total_order']

    def customer_name(self, obj):
        return obj.customer.name
    
    def total_order(self, instance):
        return instance.net_total()
    
    def total(self,instance):
        sup = 0
        Order_detail = instance.order_Detail.all()
        for order in Order_detail:
            sup += order.total_order() 
        return sup
    
    
    def dis_count(self, instance):
        dis=instance.sup_total()*instance.discount/100
        return dis

@admin.register(OrderDetail) 
class OrderDetailAdmin(admin.ModelAdmin):
    list_display=['order','product_name','quantity','price','total']

    def total(self, instance):
        return instance.total_order()
    
    def product_name(self, obj):
        return obj.product.name


# __________________________________________________________

@admin.register(StockItem) 
class StockItemAdmin(admin.ModelAdmin):
    list_display= ['__str__','name','unit','total_stock','limit','stock_limit']
    list_filter= ['name','unit','unit']
    search_fields= ['description']
    
    def total_stock(self, instance):
        return instance.stock_total()
    
    def stock_limit(self, instance):
        if instance.limit >= instance.stock_total():
            return 'Good_Stock'
        else:
            return "Out_Stock"
    
        
@admin.register(Stock_Transaction) 
class Stock_TransactionAdmin(admin.ModelAdmin):
    list_display= ['item','name','stock_in','stock_out','quantity']
    list_filter= ['item','Transaction']
    search_fields= ['item','Transaction']
    
    
    
    def name(self, obj):
        return obj.item.name
    
    def stock_in(self,obj):
        if obj.Transaction == 'Stock_In':
            return obj.Transaction
    def stock_out(self,obj):
        if obj.Transaction == 'Stock_Out':
            return obj.Transaction

    
    # def limit(self, instance):
    #     stock=instance.item.limit
    #     return stock


    
    