from django.forms import ModelForm
from booking.models import Booking# -*- coding: utf-8 -*-

class BookingForm(ModelForm):
     class Meta:
         model = Booking
         fields = ['mobile', 'address', 'delivery_date', 'item']