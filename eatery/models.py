from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    menu_name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
