from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


    



class Customer(models.Model):
    name=models.CharField(_("client"), max_length=100)
    phone=models.CharField(_("phone"), max_length=14)
    location=models.TextField(_("Address"), max_length=300)
    
    def __str__(self) :
        return f"""{self.name}"""




class Product(models.Model):
    name = models.CharField(_('name'),max_length=50)
    image = models.ImageField(_('image'),upload_to='products',null=True,blank=True)
    price = models.FloatField(_('price'),default=0)
    sku = models.CharField(_('sku'),max_length=10)
    subtitle = models.CharField(_('subtitle'),max_length=300)
    
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
    # user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    code=models.CharField(_("Order"), max_length=50,null=True,blank=True)
    status = models.CharField(_("Status"),max_length=12,choices=ORDER_STATUS,default=ORDER_STATUS[0][0])
    customer = models.ForeignKey(Customer,related_name='order_customer',on_delete=models.SET_NULL,null=True,blank=True)
    order_date = models.DateField(_("Order_date"),default=timezone.now)
    delivery_date = models.DateField(_("Delivery_date"),null=True,blank=True)
    discount=models.IntegerField(_("Discount"),null=True , blank=True,default=0)
    Delivery_Fee=models.FloatField(_("Delivery_Fee"),null=True , blank=True,default=0)
    slug=models.SlugField(null=True,blank=True)

    def __str__(self) :
        return f"""Ord-00{self.id}"""
    
    # def save(self, *args, **kwargs):
        
    #     super(Order, self).save(*args, **kwargs)
# @receiver(post_save,sender=Order)
# def create_profile(sender,instance,created,**kwargs):
#     if created:
#         Profile.objects.create(
#             user=instance
#         )
    def save(self, *args, **kwargs):
        if  self.id:
            self.code=f"""Ord-00{self.id}"""
        super(Order, self).save(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        if  self.id:
            self.slug = slugify(self.code)
        super(Order, self).save(*args, **kwargs)


        
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
        net_total=total-int(total*self.discount)/100+int(self.Delivery_Fee)
        return net_total
    
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_Detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,verbose_name='product',related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(_("Quantity"),default=1)
    price = models.FloatField(_("Price"),default=0)

    
    def __str__(self):
        return str(self.order)

    def total_order(self):
        order_total=int(self.quantity)*int(self.price)
        return order_total





UNITS=(('عدد','عدد'),('كيلو','كيلو'),('روزمة','روزمة'))
class StockItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    unit=models.CharField( max_length=50,choices=UNITS)
    limit=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        code=f"""{self.id}-{self.name}"""
        return code
    
    def stock_total(self):
        in_total =0
        out_total=0 
        stock_total=0
        stock_detail = self.Stock_Transaction.all()
        for stock in stock_detail:
            if stock.Transaction=='Stock_In':
                in_total+=stock.quantity
            else:
                out_total+=stock.quantity
        stock_total = stock_total+in_total-out_total
        return stock_total  
        

TRANSACTION=(('Stock_In','Stock_In'),('Stock_Out','Stock_Out'))
class Stock_Transaction(models.Model):
    item = models.ForeignKey(StockItem, related_name='Stock_Transaction',verbose_name=("item"), on_delete=models.CASCADE)
    Transaction=models.CharField( max_length=50,choices=TRANSACTION)
    quantity = models.IntegerField()
    

    def __str__(self) :
        return str(self.item)

