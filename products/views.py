from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product



class ProductListView(ListView):

    model = Product
    template_name = 'products/products.html'


    def __str__(self):
        return self.name

    def get_context_data(self, *, object_list=None, **kwargs):
        context = dict()
        context['productlist'] = Product.objects.all()
        return context


