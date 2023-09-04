from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # Логика для домашней страницы
    return render(request, 'Catalog/home.html')


def contact(request):
    # Логика для страницы с контактной информацией
    return render(request, 'Catalog/contact.html')