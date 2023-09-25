from django.contrib import admin
from Catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')  # Добавлены поля name и price
    list_filter = ('category', 'price')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Moderator').exists():
            return ['name', 'price', 'created_at', 'last_modified']  # Исправлены поля date_of_creation и last_change_date на created_at и last_modified
        return []