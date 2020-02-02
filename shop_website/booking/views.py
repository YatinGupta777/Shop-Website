from django.shortcuts import render
from django.shortcuts import redirect
from booking.models import Booking
from .forms import BookingForm 

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
            entry = form.save(commit=False)
            entry.save()
            return redirect('booking_index')
    else:
        form = BookingForm()
    
    return render(request,'booking_form.html',{'form':form})
    