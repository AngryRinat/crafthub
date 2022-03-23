from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def get_context_data(self, *args, **kwargs):
        context = dict()
        context["products"] = Product.objects.all()
        return context