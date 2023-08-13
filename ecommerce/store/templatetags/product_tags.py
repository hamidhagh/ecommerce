from django import template

from ..models import Product

register = template.Library()

@register.filter
def ascending_price_tag():
    return Product.objects.ascending_price()


@register.filter
def descending_price_tag():
    return Product.objects.descending_price()

