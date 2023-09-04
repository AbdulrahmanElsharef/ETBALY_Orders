from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.utils.text import slugify
# from django.db.models.signals import post_save
# from django.dispatch import receiver


    

class Designer(models.Model):
    name=models.CharField(_("Name"), max_length=50)
    phone=models.CharField(_("Phone"), max_length=14,default='No_Phone')
    note=models.CharField(_("Note"), max_length=50,default='No_Note')

    def __str__(self) :
        return f"""{self.name}"""
    


class Customer(models.Model):
    company=models.CharField(_("Company"), max_length=100)
    client=models.CharField(_("Client"), max_length=100)
    phone=models.CharField(_("Phone"), max_length=14)
    location=models.TextField(_("Address"), max_length=300)
    email=models.CharField(_("Email"), max_length=50 ,default='No_Email')
    note=models.CharField(_("Note"), max_length=50,default='No_Note')

    def __str__(self) :
        return f"""{self.company}"""




class Product(models.Model):
    name = models.CharField(_('Name'),max_length=50)
    subtitle = models.TextField(_('Subtitle'),max_length=300,default='No_Subtitle')
    note=models.CharField(("note"), max_length=50,default='No_Note')
    def __str__(self) :
        return f"""{self.name}"""
    
    
Customer_Active = (
    ('WhatsApp' , 'WhatsApp') , 
    ('FaceBook' , 'FaceBook') , 
)   
ORDER_STATUS = (
    ('Created' , 'Created') , 
    ('Confirmed' , 'Confirmed') , 
    ('Processed' , 'Processed'),
    ('Delivered','Delivered') ,
    ('Returned','Returned'), 
)
ORDER_Branch = (
    ('Etbaly_Shokran' , 'Etbaly_Shokran') , 
    ('Melouk_Eltibah' , 'Melouk_Eltibah') , 
    ('Print_Square' , 'Print_Square'),
)

class Order(models.Model):
    branch=models.CharField(_("Branch"), max_length=50,choices=ORDER_Branch)
    status = models.CharField(_("Status"),max_length=12,choices=ORDER_STATUS,default=ORDER_STATUS[0][0])
    active=models.CharField(_("Client_Active"), max_length=50,choices=Customer_Active)
    customer = models.ForeignKey(Customer,related_name='order_customer',on_delete=models.SET_NULL,null=True,blank=True)
    designer=models.ForeignKey(Designer,related_name='order_Designer',on_delete=models.SET_NULL,null=True,blank=True)
    order_date = models.DateField(_("Order_date"),default=timezone.now)
    delivery_date = models.DateField(_("Delivery_date"),null=True,blank=True)
    discount=models.IntegerField(_("Discount"),null=True , blank=True,default=0)
    Delivery=models.IntegerField(_("Delivery"),null=True , blank=True,default=0)
    note=models.CharField(("note"), max_length=50,default='No_Note')
        
    def __str__(self) :
        return f"""Ord-00{self.id}"""

    
    def net_total(self):
        total = 0
        Order_detail = self.order_Detail.all()
        for order in Order_detail:
            total += order.total_order() 
        net_total=round(total-int(self.discount)+int(self.Delivery),2)
        return net_total
    
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_Detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,verbose_name='product',related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(_("Quantity"))
    price = models.FloatField(_("Price"))
    note=models.CharField(("note"), max_length=50,default='No_Note')

    
    def __str__(self):
        return str(self.order)

    def total_order(self):
        order_total=int(self.quantity)*int(self.price)
        return order_total





