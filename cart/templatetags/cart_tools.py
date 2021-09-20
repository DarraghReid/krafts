from django import template


# "register" is instance of template.Library
register = template.Library()


# Register function as a template filter using register.filer decorator
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculate subtotal for display in cart """
    return price * quantity
