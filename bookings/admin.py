from django.contrib import admin
from .models import Resource, Booking

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    # Какие колонки показывать в списке
    list_display = ('id', 'name', 'capacity')
    # По каким полям можно искать
    search_fields = ('name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('resource', 'user', 'start_time', 'end_time')
    # Фильтры справа (по ресурсу и времени)
    list_filter = ('resource', 'start_time')

# Register your models here.
