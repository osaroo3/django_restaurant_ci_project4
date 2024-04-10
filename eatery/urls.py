from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.bookings, name='bookings'),
    path('booknow/', views.booknow, name='booknow'),
    path('edit_booking/<int:booking_id>/', views.edit_booking,
         name='edit_booking'),
    path('bookings/delete_booking/<int:booking_id>/', views.booking_delete,
         name='booking_delete'),
    path('menu/', views.menu, name='menu')
]
