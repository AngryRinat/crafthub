from django.urls import path

from admins.views import *

app_name = 'admins'

urlpatterns = [
    path('', users_read, name='users_read'),
    # path('users_create/', users_create, name='users_create'),
]