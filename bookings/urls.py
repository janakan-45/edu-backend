from django.urls import path
from . import views

urlpatterns = [
    path('api/bookings/', views.create_booking, name='create-booking'),
]
