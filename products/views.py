from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product, Category

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]



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
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Product.objects.filter()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['product']
        context['menu'] = menu
        return context

class ProductCategory(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'productlist'


    def get_queryset(self):
         return Product.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория -' + str(context['productlist'][0].cat)
        context['menu'] = menu
        return context
