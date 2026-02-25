from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from bookings.models import Resource, Booking

# def index(request):
#     count = Resource.objects.count()
#     return render(request, 'index.html', {'resource_count': count})
# 
# def home(request):
#     data = {
#         'title': 'Главная страница нашего сайта',
#         'items': ['Урок по Django', 'Настройка шаблонов', 'Работа с Views'],
#     }
#     return render(request, 'index.html', context=data)

def home(request):
    resources = Resource.objects.all()
    user_bookings = []
    
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user=request.user).order_by('-start_time')
    
    data = {
        'title': 'Система бронирования',
        'resources': resources,
        'my_bookings': user_bookings, 
    }
    return render(request, 'index.html', context=data)

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        resource_name = booking.resource.name
        booking.delete()
        messages.success(request, f'Бронирование ресурса "{resource_name}" успешно отменено!')
        return redirect('home')
    
    return redirect('home')

def about(request):
    return render(request, 'about.html')
# Create your views here.
