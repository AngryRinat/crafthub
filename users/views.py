from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.urls import reverse_lazy

from products.utils import DataMixin
from django.views.generic import CreateView
from users.forms import UserRegistrationForm, UserLoginForm
from users.models import User
from django.contrib.auth.views import LoginView, LogoutView



class RegisterUser(CreateView):
    form_class = UserRegistrationForm
    model = User
    template_name = 'users/register.html'
    success_url = reverse_lazy('products:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('products:index')


class LoginUser(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('products:index')


def logout_user(request):
    logout(request)
    return redirect('products:index')
