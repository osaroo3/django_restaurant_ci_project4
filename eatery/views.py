from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from .forms import BookingForm
from .models import Menu, Booking

# Create your views here.


def index(request):
    """
    This view renders the index.html page
    while also extending the base.html page
    """
    return render(request, 'eatery/index.html')


def menu(request):
    """
    This view renders the menu page
    for the users to view

    """
    menu = Menu.objects.all()

    return render(request, 'eatery/menu.html', {'menu': menu})


def bookings(request):
    """
    This view renders all the bookings made
    to a logged in user
    """
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        return render(
            request,
            'eatery/my_bookings.html',
            {'bookings': bookings}
        )
    else:
        return redirect('../accounts/signup')


def booknow(request):
    """
    This view renders the page for logged-in
    users to book reservations
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your booking was successfull.')
            return redirect('bookings')
        else:
            messages.error(request, "Please enter correct data")
            return render(request, 'eatery/book_now.html', {'form': form})

    form = BookingForm()
    return render(request, 'eatery/book_now.html', {'form': form})


def edit_booking(request, booking_id):
    """
    This view gives a logged in user
    the CRUD ability to edit previous bookings
    """
    booking_record = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'You succesfully modified your booking.')
            return redirect('bookings')
        else:
            return render(request, 'eatery/edit_booking.html', {'form': form})
    form = BookingForm(instance=booking_record)
    return render(
        request,
        'eatery/edit_booking.html',
        {'form': form, 'booking_record': booking_record})


def booking_delete(request, booking_id):
    """
    This view gives a logged in user
    the CRUD ability to delete previous bookings
    """
    booking_record = get_object_or_404(Booking, id=booking_id)
    if booking_record.user == request.user:
        booking_record.delete()
        messages.success(request, 'Booking deleted succesfully.')
        return redirect('bookings')
