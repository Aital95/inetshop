from django.core.management.base import BaseCommand
from Catalog.models import Category


class Command(BaseCommand):
    help = 'Fill the database with initial data'

    def handle(self, *args, **kwargs):
        # Очистка данных
        Category.objects.all().delete()

        # Заполнение данными
        Category.objects.create(name='Категория 1', description='Описание категории 1')
        Category.objects.create(name='Категория 2', description='Описание категории 2')
