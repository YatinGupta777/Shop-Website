from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Booking(models.Model):
    bill_no = models.TextField(null=True,blank=True,)
    mobile = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    billing_date = models.DateField(null=True,blank=True)
    delivery_date = models.DateField(null=True,blank=True)
  
    discount = models.IntegerField(null=True,blank=True)
    final_amount = models.IntegerField(null=True,blank=True)
    
    

        