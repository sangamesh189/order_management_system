from django.db import models

# Create your models here.

from orders.models import order
from products.models import product

class orderitem (models.Model):
    order = models.ForeignKey(order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(product,on_delete=models.SET_NULL,null=True)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.product_name} - {self.order}"
    
    