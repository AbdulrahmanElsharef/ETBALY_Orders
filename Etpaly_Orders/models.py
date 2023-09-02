from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.utils.text import slugify
# from django.db.models.signals import post_save
# from django.dispatch import receiver


    



class Customer(models.Model):
    name=models.CharField(_("client"), max_length=100)
    phone=models.CharField(_("phone"), max_length=14)
    location=models.TextField(_("Address"), max_length=300)
    email=models.EmailField(_("email"), max_length=50 ,default='no email')
    note=models.CharField(_("note"), max_length=50,default='no note')

    def __str__(self) :
        return f"""{self.name}"""




class Product(models.Model):
    name = models.CharField(_('name'),max_length=50)
    price = models.FloatField(_('price'),default=0)
    sku = models.CharField(_('sku'),max_length=10)
    subtitle = models.CharField(_('subtitle'),max_length=300)
    note=models.CharField(("note"), max_length=50,default='no note')
    def __str__(self) :
        return f"""{self.name}"""
    

    

    
ORDER_STATUS = (
    ('Created' , 'Created') , 
    ('Confirmed' , 'Confirmed') , 
    ('Processed' , 'Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered') , 
)

class Order(models.Model):
    status = models.CharField(_("Status"),max_length=12,choices=ORDER_STATUS,default=ORDER_STATUS[0][0])
    customer = models.ForeignKey(Customer,related_name='order_customer',on_delete=models.SET_NULL,null=True,blank=True)
    order_date = models.DateField(_("Order_date"),default=timezone.now)
    delivery_date = models.DateField(_("Delivery_date"),null=True,blank=True)
    discount=models.IntegerField(_("Discount"),null=True , blank=True,default=0)
    Delivery_Fee=models.FloatField(_("Delivery_Fee"),null=True , blank=True,default=0)
    note=models.CharField(("note"), max_length=50,default='no note')
        
    def __str__(self) :
        return f"""Ord-00{self.id}"""


        
    def sup_total(self):
        sup= 0
        Order_detail = self.order_Detail.all()
        for order in Order_detail:
            sup += order.total_order() 
        self.sup_total=sup
        return self.sup_total
    
    def net_total(self):
        total = 0
        Order_detail = self.order_Detail.all()
        for order in Order_detail:
            total += order.total_order() 
        net_total=round(total-int(total*self.discount)/100+int(self.Delivery_Fee),2)
        return net_total
    
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_Detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,verbose_name='product',related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(_("Quantity"),default=1)
    price = models.FloatField(_("Price"),default=0)
    note=models.CharField(("note"), max_length=50,default='no note')

    
    def __str__(self):
        return str(self.order)

    def total_order(self):
        order_total=int(self.quantity)*int(self.price)
        return order_total





