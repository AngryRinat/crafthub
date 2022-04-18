from django.urls import path

from baskets.views import basketapp

app_name = 'baskets'

urlpatterns = [
    path('', basketapp, name='baskets'),
]