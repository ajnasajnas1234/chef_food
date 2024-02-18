from django.contrib import admin
from .models import Reservation, Contact

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_no', 'date', 'time', 'no_of_people', 'message')
    list_filter = ('date', 'time')  # Add filters for date and time fields
    search_fields = ('name', 'email', 'phone_no', 'message')  # Add search functionality for specified fields

admin.site.register(Reservation, ReservationAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email', 'subject', 'contact_message')
    

admin.site.register(Contact, ContactAdmin)
