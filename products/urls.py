from django.urls import path

from products.views import ProductListView, ProductDetailView,ProductCategory

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product'),
    path('category/<slug:cat_slug>/', ProductCategory.as_view(), name='category'),
]