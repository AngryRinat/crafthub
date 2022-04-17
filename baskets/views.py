from django.shortcuts import render
from django.views.generic import ListView
from baskets.models import Basket
from users.models import User





class UserBaskets(ListView):
    model = Basket
    template_name = 'baskets/baskets.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(id=1)
        context['basketlist'] = Basket.objects.filter(user=user)
        return dict(list(context.items()))