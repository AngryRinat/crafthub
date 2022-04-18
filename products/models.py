from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('products:category', kwargs={'cat_slug': self.slug})


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products_images', blank=True)
    in_stock = models.BooleanField(default=False, verbose_name='В наличии')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории', default='1')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product', kwargs={'product_slug': self.slug})

    class Meta:
        ordering = ['id']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
