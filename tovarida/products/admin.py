from django.contrib import admin

from products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админ-модель категорий."""


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админ-модель товаров."""
