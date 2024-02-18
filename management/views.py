from django.shortcuts import render
from django.http import HttpResponse
from .models import Reservation, Contact
from . import models
import time
def index(request):
    return render(request , 'index.html')



def table_reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        number = request.POST.get('people')  # Corrected from 'number'
        message = request.POST.get('message')

        data = Reservation(name=name, phone_no=phone, email=email, date=date, time=time, no_of_people=number, message=message)
        data.save()
        print(data)
          # Delay page refresh
        return render(request, 'index.html')

    else:
        return render(request, 'index.html')
    



def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = Contact(contact_name=name, contact_email=email, subject=subject, contact_message=message)
        data.save()
        print(data)
          # Delay page refresh
        return render(request, 'index.html')

    else:
        return render(request, 'index.html')


