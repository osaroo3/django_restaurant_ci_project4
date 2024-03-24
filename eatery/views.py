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