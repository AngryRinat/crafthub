from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

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


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def basket_edit(request, pk, qty):
    if is_ajax(request=request):
        quantity = int(qty)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if qty > 0:
            new_basket_item.qty = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basketlist = Basket.objects.filter(user=request.user)

        context = {
            'basketlist': basketlist,
        }

        result = render_to_string('baskets/basket-list.html', context)

        return JsonResponse({'result': result})


def basket_remove(request):
    if is_ajax(request=request):
        basketlist = Basket.objects.filter(user=request.user)
        for b in basketlist:
            b.qty = b.qty*100
            b.save()
        context = {
            'basketlist': basketlist,
        }

        result = render_to_string('baskets/basket-list.html', context)

        return JsonResponse({'result': result})

