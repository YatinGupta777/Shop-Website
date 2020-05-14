from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking_index, name = "booking_index"),
    path("new/", views.booking_form, name = "booking_form"),
    path("reports/", views.booking_report, name = "booking_report"),
    
]


