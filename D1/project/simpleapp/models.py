from django.db import models
from django.core.validators import MinValueValidator


# Создаём модель товара
class Product(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    # поле категории будет ссылаться на модель категории
    # все продукты в категории будут доступны через поле products
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products')


    def __str__(self):
        return f'{self.name}: {self.quantity}'


#  создаём категорию, к которой будет привязываться товар
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)  # названия категорий тоже не должны повторяться

    def __str__(self):
        return f'{self.name}'