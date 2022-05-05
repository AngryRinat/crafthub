from django.contrib.auth.decorators import login_required

from products.utils import DataMixin
from django.views.generic import ListView, DetailView
from products.models import Product, Category






class ProductListView(ListView):
    paginate_by = 2
    model = Product
    template_name = 'products/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productlist'] = Product.objects.all()
        context['categorylist'] = Category.objects.all()
        context['title'] = 'Главная страница'
        return context

    # def get_queryset(self):
    #
    #     return Product.objects.all()




class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'



    def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            context['productlist'] = Product.objects.all()
            context['categorylist'] = Category.objects.all()
            return context




class ProductCategory(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'productlist'

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория -'
        return context
