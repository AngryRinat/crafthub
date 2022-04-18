from django.urls import path

from baskets.views import basketapp, basket_add

app_name = 'baskets'

urlpatterns = [
    path('', basketapp, name='baskets'),
    path('basket_add/<int:product_id>', basket_add, name='basket_add'),
]