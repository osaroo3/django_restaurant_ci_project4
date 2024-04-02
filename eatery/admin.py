from django.contrib import admin
from .models import Menu, Booking

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'price')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'table_choice', 'date', 'time')
    search_fields = ('name', 'menu', 'phone')
    list_filter = ('name', 'menu', 'created_on')