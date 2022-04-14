from django.urls import path

from users.views import RegisterUser, LoginUser, logout_user

app_name = 'users'

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]