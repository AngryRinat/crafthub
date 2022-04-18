from django.shortcuts import render
from django.views.generic import ListView
from baskets.models import Basket
from users.models import User




def basketapp(request):
    basketlist = Basket.objects.filter(user=request.user)
    title = f'Корзина для {request.user}'
    context = {
        'basketlist':basketlist,
        'title': title
    }
    return render(request, 'baskets/baskets.html', context)