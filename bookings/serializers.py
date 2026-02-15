from rest_framework import serializers
from .models import Resource, Booking
from django.utils import timezone

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'resource', 'user', 'start_time', 'end_time']

    def validate(self, data):
        """Проверка, что время начала раньше времени конца и место не занято."""
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("Конец бронирования должен быть позже начала.")
        
        if data['start_time'] < timezone.now():
            raise serializers.ValidationError("Нельзя бронировать в прошлом!")

        # Ищем существующие брони на это же время для этого ресурса
        overlapping_bookings = Booking.objects.filter(
            resource=data['resource'],
            start_time__lt=data['end_time'],
            end_time__gt=data['start_time']
        )

        if overlapping_bookings.exists():
            raise serializers.ValidationError("Это место уже забронировано на выбранное время.")
        
        return data