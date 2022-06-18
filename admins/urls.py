from django.urls import path

from admins.views import *

app_name = 'admins'

urlpatterns = [
    path('', AdminsIndexView.as_view(), name='admins_index'),
    path('users_read', AdminsUserView.as_view(), name='users_read'),
    path('users_create', admins_create_user, name='users_create'),
    path('users_delete/<int:pk>/', UserDeleteView.as_view(), name='users_delete'),
]