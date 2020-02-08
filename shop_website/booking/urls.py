from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking_index, name = "booking_index"),
    path("new/", views.booking_form, name = "booking_form"),
    #path("new/<int:pk>", views.add_item_to_booking, name = "booking_form_pk"),
]


