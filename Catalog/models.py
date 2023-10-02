from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)  # Наименование продукта
    description = models.TextField()  # Описание продукта
    image = models.ImageField(upload_to='product_images/')  # Изображение продукта (превью)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) # Категория продукта
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена за покупку
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    last_modified = models.DateTimeField(auto_now=True)  # Дата изменения
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    def __str__(self):
        return f'{self.name}, {self.description}, {self.category}, {self.price}' \
               f' {self.created_at}, {self.last_modified}'

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Category(models.Model):
    name = models.CharField(max_length=255)  # Наименование категории
    description = models.TextField()  # Описание категории

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
