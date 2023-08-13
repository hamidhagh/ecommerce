from django import template

from ..models import Product

register = template.Library()

@register.filter
def ascending_price_tag():
    return Product.objects.ascending_price()


@register.filter
def descending_price_tag():
    return Product.objects.descending_price()


@register.filter
def persian_numbers(number):
    
    english_numbers = "0123456789"
    
    persian_numbers = "۰۱۲۳۴۵۶۷۸۹"
    
    number = str(number)
    
    convert_e_to_p_numbers = number.maketrans(english_numbers, persian_numbers)
    
    return number.translate(convert_e_to_p_numbers)

