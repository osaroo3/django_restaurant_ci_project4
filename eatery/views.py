from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Menu, Booking

# Create your views here.

def index(request):
    """This view renders the index.html page
    and extends the base.html page
    """
    return render(request, 'eatery/index.html')


def menu(request):
    menu = Menu.objects.all()

    return render(request, 'eatery/menu.html', {'menu': menu})


def bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'eatery/my_bookings.html', {'bookings': bookings})


def book_now(request):
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            return redirect('bookings')
        else:
            messages.error(request, "Please input correct data")
            return render(request, 'book_now.html', {'form': form})
    form = BookingForm()
    return render(request, 'book_now.html', {'form': form})