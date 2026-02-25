from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]