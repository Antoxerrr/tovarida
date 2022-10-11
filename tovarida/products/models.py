from django.db import models

from utils.base.models import BaseModel


class Category(BaseModel):
    """Модель категории товара."""

    name = models.CharField('Наименование', max_length=64)

    def __str__(self):
        return f'Категория {self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(BaseModel):
    """Модель товара."""

    name = models.CharField('Наименование', max_length=256)
    price = models.PositiveIntegerField('Стоимость')
    categories = models.ManyToManyField(Category, verbose_name='Категории')

    def __str__(self):
        return f'Товар ({self.name})'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductPicture(BaseModel):
    """Модель изображения товара."""

    product = models.ForeignKey(
        Product, verbose_name='Товар', on_delete=models.CASCADE
    )
    picture = models.ImageField('Изображение')

    def __str__(self):
        return f'Изображение товара {self.product.name} ({self.pk})'

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'
