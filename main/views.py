from django.shortcuts import render
from bookings.models import Resource

def index(request):
    count = Resource.objects.count()
    return render(request, 'index.html', {'resource_count': count})

def home(request):
    data = {
        'title': 'Главная страница нашего сайта',
        'items': ['Урок по Django', 'Настройка шаблонов', 'Работа с Views'],
    }
    return render(request, 'index.html', context=data)

def about(request):
    return render(request, 'about.html')
# Create your views here.
