from django.db import models

# Create your models here.
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

