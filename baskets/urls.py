from django.urls import path

from baskets.views import userbaskets

app_name = 'baskets'

urlpatterns = [
    path('', userbaskets, name='baskets'),
]