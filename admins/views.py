from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
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


class AdminsDeleteView(DeleteView):
    model = User
    template_name = 'admins/users_delete.html'



class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/users_read.html'
    success_url = reverse_lazy('admins:admin_index')


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())























# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request, 'admins/base.html')
#
#
# class UserListView(ListView):
#     model = User
#     template_name = 'admins/users_read.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(UserListView, self).get_context_data(**kwargs)
#         context['title'] = 'GeekShop - Админ | Пользователи'
#         return context
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, request, *args, **kwargs):
#         return super(UserListView, self).dispatch(request, *args, **kwargs)


# class UserCreateView(CreateView):
#     model = User
#     template_name = 'admins/admin-users-create.html'
#     form_class = UserAdminRegisterForm
#     success_url = reverse_lazy('admins:admin_users')
#
#
# class UserUpdateView(UpdateView):
#     model = User
#     template_name = 'admins/admin-users-update-delete.html'
#     form_class = UserAdminProfileForm
#     success_url = reverse_lazy('admins:admin_users')
#
#
