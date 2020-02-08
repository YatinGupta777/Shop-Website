from django.shortcuts import render
from django.shortcuts import redirect
from booking.models import Booking
from .forms import *

def booking_index(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'bookings_index.html', context)

def booking_form(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid(): 
            form.discount = request.POST.get('discount')
            form.final_amount = request.POST.get('final_amount')
            entry = form.save(commit=False)
            entry.save()
            return redirect('booking_index')
    else:
        form = BookingForm()
    
    return render(request,'booking_form.html',{'form':form})
    
# =============================================================================
# def add_item_to_booking(request, pk):
#     bill_no = get_object_or_404(Booking, pk=pk)
#     if request.method == "POST":
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.bill_no = bill_no
#             item.save()
#             return redirect('booking_form_pk.html', pk=bill_no.pk)
#     else:
#         form = ItemForm()
#     return render(request, 'booking_form_pk.html', {'form': form})
# =============================================================================
