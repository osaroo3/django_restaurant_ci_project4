from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.bookings, name='bookings'),
    path('menu/', views.menu, name='menu')
]