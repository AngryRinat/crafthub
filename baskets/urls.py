from django.urls import path

from baskets.views import UserBaskets

app_name = 'baskets'

urlpatterns = [
    path('', UserBaskets.as_view(), name='baskets'),
]