from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from baskets.models import Basket
from products.models import Product



def basketapp(request):
    basketlist = Basket.objects.filter(user=request.user)
    title = f'Корзина для {request.user}'
    context = {
        'basketlist':basketlist,
        'title': title
    }
    return render(request, 'baskets/baskets.html', context)

def basket_add(request, product_id):
    product = Product.object.get(id=product_id)
    baskets = Basket.object.filter(user = request.user, product=product)
    if not baskets.exists:
            baskets = Basket.object.create(user=request.user, product=product, qty=1)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
            basket = baskets.first()
            basket.qty += 1
            basket.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))