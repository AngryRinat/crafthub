from django.urls import path

from baskets.views import *

app_name = 'baskets'

urlpatterns = [
    path('', basketapp, name='baskets'),
    path('basket_add/<int:product_id>', basket_add, name='basket_add'),
    path('basket_remove/', basket_remove, name='basket_remove'),
    path('basket_increase/<int:id>', basket_increase, name='basket_increase')
]