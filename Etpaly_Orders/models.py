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

class Seller(models.Model):
    name=models.CharField(_("Name"), max_length=50)
    phone=models.CharField(_("Phone"), max_length=14,default='No_Phone')
    note=models.CharField(_("Note"), max_length=50,default='No_Note')

    def __str__(self) :
        return f"""{self.name}"""
    


class Customer(models.Model):
    company=models.CharField(_("Company"), max_length=100)
    client=models.CharField(_("Client"), max_length=100)
    phone_1=models.CharField(_("Phone 1 "), max_length=14)
    phone_2=models.CharField(_("Phone 2 "), max_length=14,default='No Phone')
    location=models.TextField(_("Address"), max_length=300)
    email=models.CharField(_("Email"), max_length=50 ,default='No_Email')
    note=models.CharField(_("Note"), max_length=50,default='No_Note')
    def __str__(self) :
        return f"""{self.company}"""




class Product(models.Model):
    name = models.CharField(_('Name'),max_length=50)
    details = models.TextField(_('Details'),max_length=300,default='No_Details')
    note=models.CharField(("Note"), max_length=50,default='No_Note')
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
    seller=models.ForeignKey(Seller,related_name='order_Seller',on_delete=models.PROTECT)
    active=models.CharField(_("Active"), max_length=50,choices=Customer_Active)
    customer = models.ForeignKey(Customer,related_name='order_customer',on_delete=models.PROTECT)
    designer=models.ForeignKey(Designer,related_name='order_Designer',on_delete=models.PROTECT)
    order_date = models.DateField(_("Date"),default=timezone.now)
    transfer=models.IntegerField(_("Transfer"),default=0)
    cash=models.IntegerField(_("Cash"),default=0)
    Due_date = models.DateField(_("Due_date"),null=True,blank=True)
    discount=models.IntegerField(_("Discount"),default=0)
    Delivery=models.IntegerField(_("Delivery"),default=0)
    note=models.CharField(("Note"), max_length=50,default='No_Note')

        
    def __str__(self) :
        return f"""Ord-00{self.id}"""

    
    def net_total(self):
        total = 0
        Order_detail = self.order_Detail.all()
        for order in Order_detail:
            total += order.price 
        net_total=total-int(self.discount)+int(self.Delivery)
        return net_total
    
    def Customer_debt(self):
        Order_debt= self.net_total()-self.cash-self.transfer
        return Order_debt
    
    def total_items(self):
        total = 0
        Order_detail = self.order_Detail.all()
        for order in Order_detail:
            total +=1
        return total
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_Detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,verbose_name='product',related_name='order_product',on_delete=models.PROTECT)
    quantity = models.IntegerField(_("Quantity"),default=0)
    price = models.IntegerField(_("Price"),default=0)
    note=models.CharField(("note"), max_length=50,default='No_Note')

    
    def __str__(self):
        return str(self.order)

    # def total_order(self):
    #     order_total=int(self.quantity)*int(self.price)
    #     return order_total





