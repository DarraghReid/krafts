from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from cart.contexts import cart_contents
import stripe


def checkout(request):
    # Get public and secret keys from settings
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Get cart from session
    cart = request.session.get('cart', {})
    # If cart is empty
    if not cart:
        # Use error message to inform user the cart is empty
        messages.error(request, "There's nothing in your cart at the moment")
        # Bring user back to products page
        return redirect(reverse('products'))

    # Access cart_contents' contexts dictionary from cart's context.py
    current_cart = cart_contents(request)
    # Save grand_total's key from dictionary to total variable
    total = current_cart['grand_total']
    # Convert total to integer for Stripe
    stripe_total = round(total * 100)
    # Set secret key on Stripe
    stripe.api_key = stripe_secret_key
    # Create payment intent
    intent = stripe.PaymentIntent.create(
        # Set the amount to stripe_total above
        amount = stripe_total,
        # Set the currency to value of STRIPE_CURRENCY in settings
        currency = settings.STRIPE_CURRENCY
    )

    # Create instance of order form
    order_form = OrderForm()

    # If stripe_public_key has not been set
    if not stripe_public_key:
        # Prompt for public key to be set
        messages.warning(
            request, 'Stripe public key is missing.\
                Did you forget to set it in your environment?')

    # Create template for checkout form
    template = 'checkout/checkout.html'
    
    # Pass order form into context
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    # Render the template with order form
    return render(request, template, context)