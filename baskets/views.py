from django.shortcuts import render
from django.views.generic import ListView
from baskets.models import Basket
from products.models import Product



def userbaskets(request):
    baskets = Basket.objects.all()
    return baskets

# class UserBaskets(ListView):
#     model = User
#     template_name = 'baskets/baskets.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['basketlist'] = Basket.objects.filter(user=User.pk)
#         return dict(list(context.items()))