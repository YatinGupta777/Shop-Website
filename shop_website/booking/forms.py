from django import forms
from booking.models import Booking# -*- coding: utf-8 -*-

class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
     class Meta:
         model = Booking
         fields = ['bill_no','mobile', 'address', 'billing_date', 'delivery_date','discount','final_amount']
         widgets = {
        'bill_no': forms.Textarea(attrs={'rows':1}),
          'mobile': forms.Textarea(attrs={'rows':1}),
          'address': forms.Textarea(attrs={'rows':1}),
          'delivery_date': DateInput(),
          }

# =============================================================================
# class ItemForm(forms.ModelForm):
#      class Meta:
#          model = Items
#          fields = ['bill_no', 'item', 'quantity', 'rate']
#          widgets = {
#           'bill_no': forms.Textarea(attrs={'rows':1}),
#           }        
# =============================================================================
