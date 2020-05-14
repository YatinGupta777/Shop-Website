from django.shortcuts import render
from django.shortcuts import redirect
from booking.models import Booking
from .forms import *
from django.views import generic
from django.utils import timezone
from django.db.models import Sum


# =============================================================================
# class BookingIndex(generic.ListView):
#     model=Booking
# =============================================================================
def booking_index(request):
    bookings = Booking.objects.all().order_by("-id")[:100]
    if request.method =="POST": 
        if request.POST['action'] == 'Deliver':
            pk = request.POST.get('booking_id')
            obj = Booking.objects.get(id=pk)
            obj.delivered = True
            obj.actual_delivery_date = timezone.now()
            obj.save()
            context = {
            'bookings': bookings
            }
            return render(request, 'bookings_index.html', context)
        elif request.POST['action'] == 'Delete':
             pk = request.POST.get('booking_id')
             Booking.objects.filter(id=pk).delete()       
             bookings = Booking.objects.all().order_by("-id")[:100]
             context = {
                 'bookings': bookings
                 }
             return render(request, 'bookings_index.html', context)
         
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
            form.message = request.POST.get('message')
            entry = form.save(commit=False)
            entry.save()
            return redirect('booking_index')
    else:
        form = BookingForm()
    
    return render(request,'booking_form.html',{'form':form})

def booking_report(request):
     start_date = None
     end_date = None
     delivered = True
     if request.method =="POST": 
          if request.POST['action'] == 'Filter':
             start_date = request.POST['start_date']
             end_date = request.POST['end_date']
             delivered = request.POST.get('delivered_checkbox', '') == 'on'
             bookings = Booking.objects.filter(billing_date__range=[start_date, end_date],delivered=delivered)
             total = bookings.aggregate(Sum('final_amount'))
             context = {
                 'bookings': bookings,
                 'total' : total
                 }
             return render(request, 'booking_report.html', context)
# =============================================================================
#           elif request.POST['action'] == 'Deliver':
#             pk = request.POST.get('booking_id')
#             obj = Booking.objects.get(id=pk)
#             obj.delivered = True
#             obj.actual_delivery_date = timezone.now()
#             obj.save()
#             bookings = Booking.objects.filter(billing_date__range=[start_date, end_date],delivered=delivered)
#             context = {
#             'bookings': bookings
#             }
#             return render(request, 'booking_report.html', context)
#           elif request.POST['action'] == 'Delete':
#              pk = request.POST.get('booking_id')
#              Booking.objects.filter(id=pk).delete()       
#              bookings = Booking.objects.filter(billing_date__range=[start_date, end_date],delivered=delivered)
#              context = {
#                  'bookings': bookings
#                  }
#              return render(request, 'booking_report.html', context)
# =============================================================================
     return render(request, 'booking_report.html')   
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
