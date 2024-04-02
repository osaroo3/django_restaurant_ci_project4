from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Menu(models.Model):
    menu_name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('menu_name', 'price', )

    def __str__(self):
        return f"{self.menu_name} at £{self.price}"


HOURS = (
    ('08:00', '08:00'),
    ('08:30', '08:30'),
    ('09:00', '09:00'),
    ('09:30', '09:30'),
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
    ('22:00', '22:00'),
)

TABLE = (
    ('Table for 1', 'Table for 1'),
    ('Table for 2', 'Table for 2'),
    ('Table for 4', 'Table for 4'),
    ('Table for 6', 'Table for 6'),
    ('Table for 8', 'Table for 8'),
)

class Booking(models.Model):

    """
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{8,15}$',
                                message="Please enter a valid phone number,"
                                "e.g. 123456789. Up to 15 digits allowed.",
                                code="invalid")
    phone = models.CharField(validators=[phoneRegex], max_length=16,
                             null=True, blank=True)
    table_choice = models.CharField(max_length=50, choices=TABLE, default='Table for 1')
    date = models.DateField()
    time = models.CharField(max_length=50, choices=HOURS, default='08:00')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
        unique_together = ('user', 'date', 'time', 'menu','table_choice')

    def __str__(self):
        return f"{self.name}|{self.menu}|{self.table_choice}|{self.date}|{self.time}"
