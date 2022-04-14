from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from products.utils import DataMixin
from django.views.generic import CreateView
from users.forms import UserRegistrationForm
from users.models import User

class RegisterUser(DataMixin, SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    model = User
    template_name = 'users/register.html'
    success_url = reverse_lazy('products:index')
    success_message = 'Success!'