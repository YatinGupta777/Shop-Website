from django import forms
from booking.models import Booking# -*- coding: utf-8 -*-

class BookingForm(forms.ModelForm):
     class Meta:
         model = Booking
         fields = ['mobile', 'address', 'delivery_date', 'item']
         widgets = {
          'mobile': forms.Textarea(attrs={'rows':1}),
          'address': forms.Textarea(attrs={'rows':1}),
          }