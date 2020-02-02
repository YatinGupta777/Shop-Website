from django.db import models

# Create your models here.
class Booking(models.Model):
    mobile = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    delivery_date = models.DateField(null=True,blank=True)
    item = models.TextField(null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    rate = models.IntegerField(null=True,blank=True)
   # amount = int(rate)*int(quantity)
    discount = models.IntegerField(null=True,blank=True)
  #  final_amount = amount-discount
    paid_amount = models.IntegerField(default = 0,null=True,blank=True)
    