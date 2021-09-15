from decimal import Decimal
from django.conf import settings


def cart_contents(request):
    """ Context processor available to all templates """

    # List of cart items go here
    cart_items = []

    # Initialise total and product count
    total = 0
    product_count = 0

    # If the total price of cart contents is less than FDT
    if total < settings.FREE_DELIVERY_THRESHOLD:
        # Delivery is calculated as 10% of total
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)

        # FDD informs user how much they need to spend to hit FDT
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total

    # If total price of cart contents >= FDT
    else:
        # Delivery and FDD are irrelevant/0
        delivery = 0
        free_delivery_delta = 0

    # grand_total is bag contents plus delivery charges (if any)
    grand_total = delivery + total

    # Context processor available to all templates across site by
    # adding to context_processors in settings.py
    contexts = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return contexts
