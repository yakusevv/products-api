from django.db import models
from django.utils.translation import gettext_lazy as _

from djmoney.models.fields import MoneyField


class Category(models.Model):

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    name = models.CharField(max_length=100)


class Product(models.Model):

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('name', '-add_datetime',)

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    quantity = models.PositiveIntegerField(default=0)
    add_datetime = models.DateTimeField(auto_now_add=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)