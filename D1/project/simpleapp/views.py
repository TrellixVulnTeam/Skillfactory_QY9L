from django.shortcuts import render
from django.views.generic import ListView, DetailView
from datetime import datetime
from django.core.paginator import Paginator
# импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Product, Category
from .filters import ProductFilter


class ProductsList(ListView):
    def get(self, request):
        products = Product.objects.order_by('-price')
        p=Paginator(products,1)
        products = p.get_page(request.GET.get('page',1))
        data = {'products':products}
        return render(request, 'simpleapp/product_list.html',data)

class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

class Products(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 2 # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context