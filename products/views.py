from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'products/index.html'

    def __str__(self):
        return self.name

    def get_context_data(self, *, object_list=None, **kwargs):
        context = dict()
        context['productlist'] = Product.objects.all()
        context['categorylist'] = Category.objects.all()
        context['title'] = 'Заглавная страница'
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'

    def __str__(self):
        return self.name
