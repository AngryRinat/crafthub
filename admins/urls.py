from django.urls import path

from admins.views import *

app_name = 'adminstaff'

urlpatterns = [
    path('', adminstaff, name='index'),
]