from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils.text import slugify

    

# Create your models here.

class Customer(models.Model):
    name=models.CharField(("اسم العميل"), max_length=150)
    phone=models.CharField(("رقم التليفون"), max_length=50)
    location=models.TextField(("عنوان"), max_length=300)
    
    def __str__(self) :
        code=f"""-00{self.id}-{self.name}"""
        return code


FLAG_TYPES = (
    ('New' , 'New'),
    ('Feature' , 'Feature'),
    ('Sale' , 'Sale'),
)
class Product(models.Model):
    name = models.CharField(_('name'),max_length=120)
    image = models.ImageField(_('image'),upload_to='products')
    price = models.FloatField(_('price'))
    sku = models.IntegerField(_('sku'),)
    subtitle = models.CharField(_('subtitle'),max_length=300)
    description = models.TextField(_('description'),max_length=20000)
    flag = models.CharField(_('flag'),max_length=10,choices=FLAG_TYPES)
    slug = models.SlugField(null=True,blank=True)
    
    def __str__(self) :
        code=f"""00{self.id}-{self.name}"""
        return code
    
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Product, self).save(*args, **kwargs)
    

    
ORDER_STATUS = (
    ('Created' , 'Created') , 
    ('Confirmed' , 'Confirmed') , 
    ('Processed' , 'Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered') , 
)

class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(max_length=12,choices=ORDER_STATUS,default=ORDER_STATUS[0][0])
    customer = models.ForeignKey(Customer,related_name='order_customer',on_delete=models.SET_NULL,null=True,blank=True)
    order_time = models.DateField(default=timezone.now)
    delivery_time = models.DateField(null=True,blank=True)
    discount=models.FloatField(null=True , blank=True,default=0)
    Delivery_Fee=models.FloatField(null=True , blank=True,default=0)
    
    def __str__(self) :
        code=f"""Order-00{self.id}"""
        return code
    
    def sup_total(self):
        sup = 0
        Order_detail = self.order_Detail.all()
        for order in Order_detail:
            sup += order.total_order() 
        return sup  
    
    def net_total(self):
        total = 0
        Order_detail = self.order_Detail.all()
        for order in Order_detail:
            total += order.total_order() 
        net_total=total+int(total*self.discount)/100+int(self.Delivery_Fee)
        return net_total
    
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_Detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()

    
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
        code=f"""00{self.id}-{self.name}"""
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

