from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Resource, Booking
from .serializers import ResourceSerializer, BookingSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    # Просматривать могут все, менять — только админ
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Это магия: берем пользователя из request и передаем в метод save
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Обычный пользователь видит только свои бронирования
        # Админ видит всё
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)
    
# Create your views here.
