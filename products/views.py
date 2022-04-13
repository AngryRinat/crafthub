from products.utils import DataMixin
from django.views.generic import ListView, DetailView
from products.models import Product, Category





class ProductListView(DataMixin, ListView):
    paginate_by = 2

    model = Product
    template_name = 'products/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главая страница')
        context['productlist'] = Product.objects.all()
        context['categorylist'] = Category.objects.all()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Product.objects.all()



class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title=context['title'])
            context['productlist'] = Product.objects.all()
            context['categorylist'] = Category.objects.all()
            return dict(list(context.items()) + list(c_def.items()))

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
