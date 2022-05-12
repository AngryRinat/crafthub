from django.db import models

from products.models import Product
from users.models import User



class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    created_tampstamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.name} | Продукт {self.product.name}'

    def sum(self):
        return self.qty * self.product.price

    def total_qty(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.qty for basket in baskets)

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)