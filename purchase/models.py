from django.db import models
from products.models import LaptopProduct , UserAdmin

class CartItem(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    laptop=models.ForeignKey(LaptopProduct,on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField(default=1)
    custumer=models.ForeignKey(UserAdmin,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.laptop} - {self.quantity} - by {self.custumer}"
    

class Order(models.Model):
    customer = models.ForeignKey(UserAdmin, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True,unique=True)
    items=models.ManyToManyField(CartItem,)
    total_price=models.DecimalField(max_digits=100,decimal_places=4)
    
    status_choices = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ]

    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str: 
        return f"{self.items} -is ordered by {self.customer} - the price is {self.total_price}"
    
    def complete_order(self):
        self.status = 'completed'
        self.save()



class Payment(models.Model):
    PAYMENT_METHODS = [
        ('credit_card', 'Credit Card'),
        ('cash', 'Cash'),
        ('electronic_payment', 'Electronic Payment'),]
    
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)  
    payment_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ], default='pending')
    
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"Payment for {self.order} - {self.payment_status}"
