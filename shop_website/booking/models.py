from django.db import models
from django.utils import timezone

# Create your models here.
class Booking(models.Model):
    bill_no = models.TextField(null=True,blank=True,)
    mobile = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    billing_date = models.DateField(null=True,blank=True,default=timezone.now)
    delivery_date = models.DateField(null=True,blank=True)
  
    discount = models.IntegerField(null=True,blank=True)
    final_amount = models.IntegerField(null=True,blank=True)
    
    delivered = models.BooleanField(null=True,blank=True,default=False)
    actual_delivery_date = models.DateField(null=True,blank=True)
    
    message = models.TextField(null=True,blank=True)

        