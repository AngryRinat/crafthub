from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from users.models import User
from users.forms import UserRegistrationForm


class AdminsIndexView(TemplateView):
    template_name = 'admins/index.html'
    title = 'Админка'


class AdminsUserView(ListView):
    model = User
    template_name = 'admins/users_read.html'
    title = 'Пользователи'


def admins_create_user(request):
    if request.method == 'POST':

        form = UserRegistrationForm(data=request.POST, files=request.FILES)
        print(form.errors)
        if form.is_valid():
            print('valid')
            form.save()
            return HttpResponseRedirect(reverse('admins:admins_index'))
    else:
        form = UserRegistrationForm()

    context = {'title': 'Admin', 'form': form}
    return render(request, 'admins/users_create.html', context)


def admin_user_delete(request,pk):
    user = User.objects.get(id=pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admins_index'))

