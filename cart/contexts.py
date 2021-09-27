from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """ Context processor available to all templates """

    # List of cart items go here
    cart_items = []

    # Initialise variables
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    # For each item and quantity in session cart
    for item_id, quantity in cart.items():
        # Get the item from Product model using item id
        product = get_object_or_404(Product, pk=item_id)

        # Add item's quantity + price to total
        total += quantity * product.price

        # Increment product count by quantity
        product_count += quantity

        # Add dictionary to list of cart item details
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

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

    # grand_total is cart contents plus delivery charges (if any)
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
        'cart': cart,
    }

    return contexts
