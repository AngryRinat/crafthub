from django.http import HttpResponseRedirect
from django.shortcuts import render
from users.models import User

from django.urls import reverse


def users_read(request):
    users = User.objects.all()
    context = {'title': 'Просмотр пользователей', 'users':users}
    return render(request, 'admins/users_read.html', context)


# def users_create(request):
#     if request.method == 'POSt':
#         form =
#     context = {'title': 'Создание пользователя'}
#     return render(request, 'admins/users_create.html', context)
#
# def users_create(request):
#     if request.method == 'POST':
#         form = AdminCreateForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#     else:
#         form = AdminCreateForm()
#     context = {'title': 'GeekShop - Admin', 'form': form}
#     return render(request, 'admins/', context)