from django import forms
from .models import Booking
from django.core.validators import MinValueValidator
import datetime


def get_min_date():
    """users can book 24 hours in advance
     """
    return datetime.date.today() + datetime.timedelta(days=1)


class DateInput(forms.DateInput):
    """This class handles calendar widget for
    picking the booking date.
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """This class generates a form from the Booking model
    """

    date = forms.DateField(
        validators=[MinValueValidator(get_min_date)],
        widget=DateInput(attrs={'type': 'date', 'min': get_min_date}))

    class Meta:
        model = Booking
        fields = ('name', 'phone', 'email', 'service', 'table_choice' 'date', 'time')
        widgets = {'date': DateInput()}