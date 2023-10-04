from django.shortcuts import render, get_object_or_404
from .models import Product


def product_detail(request, product_id):
    # Получение продукта из базы данных по идентификатору product_id
    product = get_object_or_404(Product, pk=product_id)

    # Передача данных о товаре в шаблон
    context = {'product': product}

    # Вернуть шаблон с информацией о продукте
    return render(request, 'Catalog/product_detail.html', context)


def home(request):
    products = Product.objects.all()
    return render(request, 'Catalog/home.html', {'products': products})
