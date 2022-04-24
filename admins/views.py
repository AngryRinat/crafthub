from django.shortcuts import render
from users.models import User




def users_read(request):
    users = User.objects.all()
    context = {'title': 'Просмотр пользователей', 'users':users}
    return render(request, 'admins/users_read.html', context)
