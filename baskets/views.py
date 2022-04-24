from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from baskets.models import Basket
from products.models import Product
from django.template.loader import render_to_string
from django.http import JsonResponse


def basketapp(request):
    basketlist = Basket.objects.filter(user=request.user)
    title = f'Корзина для {request.user}'
    context = {
        'basketlist': basketlist,
        'title': title
    }
    return render(request, 'baskets/baskets.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        baskets = Basket.objects.create(user=request.user, product=product, qty=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        basket = baskets.first()
        basket.qty += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, id):
    basket = Basket.objects.get(id=id)

    if basket.qty > 1:
        basket.qty -= 1
        basket.save()
    else:
        basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_increase(request, id):
    basket = Basket.objects.get(id=id)

    basket.qty += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
