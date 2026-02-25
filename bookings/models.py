from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Resource(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    capacity = models.IntegerField(default=1, verbose_name="Вместимость")

    def is_currently_free(self):
        # Проверяем, есть ли хоть одно активное бронирование прямо сейчас
        now = timezone.now()
        active_booking = self.bookings.filter(start_time__lte=now, end_time__gte=now).exists()
        return not active_booking

    def __str__(self):
        return self.name

class Booking(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name="Начало брони")
    end_time = models.DateTimeField(verbose_name="Конец брони")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} забронировал {self.resource}"

# Create your models here.
