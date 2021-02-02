# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from datetime import datetime
# импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Product, Category


class ProductsList(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context
class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
