from django.shortcuts import render
from django.views.generic import ListView
from baskets.models import Basket

class UserBaskets(ListView):
    model = Basket
    template_name = 'baskets/baskets.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basketlist'] = Basket.objects.all()
        context['title'] = f'Корзина для {}'
        return dict(list(context.items()))