from django.urls import path

from products.views import ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path ('product/', ProductDetailView.as_view(), name='product')
]