from django.db import models
from django.utils import timezone


class UOM(models.Model):
    name = models.CharField('Unit', max_length=50,null=True,blank=True)
    note = models.CharField('Note', max_length=50,default='No Note',null=True,blank=True)
    def __str__(self) :
        return self.name
    
    
class Category(models.Model):
    name = models.CharField('Category', max_length=50,null=True,blank=True)
    note = models.CharField('Note', max_length=50,default='No Note',null=True,blank=True)
    def __str__(self) :
        return self.name
    
class Officer(models.Model):
    name=models.CharField(("Officer"), max_length=50,unique=True)
    phone=models.CharField(("Phone"), max_length=14,default='No_Phone')
    note=models.CharField(("Note"), max_length=50,default='No_Note')

    def __str__(self) :
        return f"""{self.name}"""
    
# Create your models here.
class StockItem(models.Model):
    name = models.CharField(max_length=100)
    des = models.CharField('Describe', max_length=50,default='No Descriptions')
    category=models.ForeignKey(Category, verbose_name=("Category"), on_delete=models.DO_NOTHING)
    unit=models.ForeignKey(UOM, verbose_name=("Unit"), on_delete=models.DO_NOTHING)
    price=models.FloatField(("Price"))
    created_at = models.DateField(("Date"),default=timezone.now)
    note=models.CharField(("Note"), max_length=50,default='No_Note')

    
    def __str__(self) :
        return self.name
    
    
    def code(self):
        code=f"""Item-00{self.id}"""
        return code
    
    def stock_total(self):
        in_total =0
        out_total=0 
        stock_detail = self.Stock_Transaction.all()
        for stock in stock_detail:
            if stock.transaction=='Stock_In':
                in_total+=stock.quantity
            elif stock.transaction=='Stock_Out':
                out_total+=stock.quantity
        stock_total = in_total-out_total
        return stock_total
    
    def stock_price(self):
        in_total =0
        out_total=0 
        stock_detail = self.Stock_Transaction.all()
        for stock in stock_detail:
            if stock.transaction=='Stock_In':
                in_total+=stock.quantity
            elif stock.transaction=='Stock_Out':
                out_total+=stock.quantity
        stock_total = in_total-out_total
        stock_price=stock_total*self.price
        return stock_price
        

TRANSACTION=(('Stock_In','Stock_In'),('Stock_Out','Stock_Out'))
class Transaction(models.Model):
    transaction = models.CharField( max_length=50,choices=TRANSACTION)
    officer = models.ForeignKey(Officer,related_name='Transaction_Officer',on_delete=models.PROTECT)
    item = models.ForeignKey(StockItem,verbose_name=("item"),related_name='Stock_Transaction', on_delete=models.CASCADE)
    quantity = models.FloatField("Quantity")
    date = models.DateField(("Date"),default=timezone.now)
    note =models.CharField(("Note"), max_length=50,default='No_Note')

    

    def __str__(self) :
        return str(self.item)

