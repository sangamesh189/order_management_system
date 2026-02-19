from django.db import models

# Create your models here.
from users.models import CustomUser

class order(models.Model):
    status_choice = [
        ('pending', 'Pending'),
        ('placed', 'Placed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]
    refund_status_choice = [
        ('none', 'None'),
        ('initiated', 'Initiated'),
        ('processed', 'Processed'),
        ('failed', 'Failed'),
    ]

    unique_id = models.CharField(max_length=100,unique=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='orders')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    address = models.TextField()
    status = models.CharField(max_length=20,choices=status_choice,default='pending')
    refund_status = models.CharField(max_length=255,choices=refund_status_choice,default='none')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cancelled_at = models.DateTimeField(blank=True,null = True)

    def __str__(self):
        return self.unique_id
    
    