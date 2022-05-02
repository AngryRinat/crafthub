from django.urls import path

from baskets.views import *

app_name = 'baskets'

urlpatterns = [
    path('', basketapp, name='baskets'),
    path('basket_add/<int:product_id>', basket_add, name='basket_add'),
    path('edit/<int:pk>/<int:qty>/', basket_edit, name='edit'),
    path('remove', basket_remove, name='remove')
]